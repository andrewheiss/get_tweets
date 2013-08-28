# get_tweets: Display your most recent tweet with jQuery and Python

Version 1.1 of the Twitter API requires all API calls to go through OAuth authentication, which breaks lots of Javascript and jQuery plugins that display recent tweets (such as [twitterjs](https://code.google.com/p/twitterjs/)). This simple web application works around that limitation by making an authenticated API query with a Python script and returning it as HTML through a jQuery Ajax function. It's a little convoluted, but it works.

## Instructions

1. Create a new application at [Twitter's Developer Center](https://dev.twitter.com/).
2. Make note of the application's consumer key and consumer secret and your user's access token and access secret.
3. Rename `get_tweets.conf.sample` to `get_tweets.conf` and paste in your consumer and access tokens and keys.
4. Place `get_tweets.py` and `get_tweets.conf` on your server somewhere. I put the script in `public_html/get_tweets` and the configuration file in a directory that's not publicly accessible on the server.
5. Update the path to the configuration file in `get_tweets.py` (near line 9: `config.read("/full/path/to/get_tweets.conf")`)
6. Install `tweepy` and `babel` on the server using `pip install tweepy` and `pip install babel`.
7. Ensure `mod_wsgi` is installed and activated on your Apache server.
8. In your site's virtual hosts file or in `.htaccess`, create a `WSGIScriptAlias` like so:  
    `WSGIScriptAlias /get_tweets /full/path/to/get_tweets.py`
9. Visit http://example.com/get_tweets and you *should* (in theory) see HTML output of your most recent tweet.
10. Modify `get_tweets.js` to point to the script URL (by default `/get_tweets/`).
11. Create an HTML element with `id=twitter`.
12. Include jQuery and `get_tweets.js` in your HTML page.
13. Voila! Through the magic of jQuery and Ajax, the content of the `#twitter` element should be replaced with your most recent tweet.


## License

`get_tweets` is free and open source software and is provided under the MIT license

Copyright (C) 2013 Andrew Heiss

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
