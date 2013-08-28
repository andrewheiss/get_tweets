#!/usr/bin/env python
import tweepy
import ConfigParser
from datetime import datetime
from babel.dates import format_timedelta

# Load configuration file
config = ConfigParser.ConfigParser()
config.read("get_tweets.conf")

# Connect to Twitter
def login():
  consumer_key = config.get('twitter_login', 'consumer_key')
  consumer_secret = config.get('twitter_login', 'consumer_secret')
  access_token = config.get('twitter_login', 'access_token')
  access_secret = config.get('twitter_login', 'access_secret')

  auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_secret)
  return(auth)

# Adapted from https://github.com/ryanmcgrath/twython/blob/173adee4a68b3a01292a3878e7fc33fa9622ee32/twython/api.py
def htmlize_tweet(tweet, use_display_url=True, use_expanded_url=False):
  if tweet.entities:
    text = tweet.text
    entities = tweet.entities

    # Mentions
    for entity in entities['user_mentions']:
      start, end = entity['indices'][0], entity['indices'][1]

      mention_html = '<a href="https://twitter.com/{screen_name}">@{screen_name}</a>'.format(screen_name = entity['screen_name'])
      text = text.replace(tweet.text[start:end], mention_html)

    # Hashtags
    for entity in entities['hashtags']:
      start, end = entity['indices'][0], entity['indices'][1]

      hashtag_html = '<a href="https://twitter.com/search?q=%23{hashtag}">#{hashtag}</a>'.format(hashtag = entity['text'])
      text = text.replace(tweet.text[start:end], hashtag_html)

    # Urls
    for entity in entities['urls']:
      start, end = entity['indices'][0], entity['indices'][1]
      if use_display_url and entity.get('display_url'):
        shown_url = entity['display_url'].encode('utf-8')
      elif use_expanded_url and entity.get('expanded_url'):
        shown_url = entity['expanded_url'].encode('utf-8')
      else:
        shown_url = entity['url'].encode('utf-8')
      print(shown_url)

      url_html = '<a href="{url}">{shown_url}</a>'.format(url=entity['url'], shown_url=shown_url).decode('utf-8')
      text = text.replace(tweet.text[start:end], url_html)

  return text

# Log in to Twitter
auth = login()
api = tweepy.API(auth)

# Format the output HTML
html_out = '<ul>\n'

for tweet in api.user_timeline(exclude_replies = True, include_rts = False, count = 1, include_entities=True):
  timestamp = (format_timedelta(datetime.now() - tweet.created_at, locale='en_US'))
  print(tweet.__dict__)
  # print(type(htmlize_tweet(tweet)))
  template = u'\t<li>{text} <a href="http://twitter.com/{twitter_name}/statuses/{tweet_id}/" class="twitter_timestamp">{timestamp} ago</a></li>'.format(text=htmlize_tweet(tweet), twitter_name=tweet.user.screen_name, tweet_id=tweet.id, timestamp=timestamp).encode('utf-8')
  html_out += template + '\n'

html_out += '</ul>'
print(html_out)

# Write tweet to a file
# with open(config.get('options', 'destination_file'), 'w') as f:
  # f.write(html_out)

def application(environ, start_response):
  status = '200 OK'
  output = html_out

  response_headers = [('Content-type', 'text/plain'),
  ('Content-Length', str(len(output)))]
  start_response(status, response_headers)

  return [output]
