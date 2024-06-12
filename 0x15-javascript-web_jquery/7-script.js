// Make sure that the DOM is loaded before running the script
$(document).ready(function() {
  // Fetch the character name from the provided URL
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(data) {
    // Display the char name in the DIV#character element
    $('#character').text(data.name);
  });
});

