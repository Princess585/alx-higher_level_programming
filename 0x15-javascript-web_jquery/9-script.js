// Make sure that the script runs when the DOM is loaded
$(document).ready(function() {
  // Fetch the translation of "hello" from the provided URL
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
    // Display the value of "hello" in the DIV#hello element
    $('#hello').text(data.hello);
  });
});

