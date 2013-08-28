$(document).ready(function () {
  $.ajax({
    url: "/get_tweets/",
    cache: false,
    dataType: "html",
    success: function(data) {
      $("#twitter").html(data);
    }
  });
});
