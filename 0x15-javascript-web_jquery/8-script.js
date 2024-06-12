// Make sure that the DOM is loaded before running the script
$(document).ready(function() {
  // Fetch the list of movies from the provided URL
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
    // Iterate over the list of movies and append each title to the UL#list_movies element
    data.results.forEach(function(movie) {
      $('#list_movies').append('<li>' + movie.title + '</li>');
    });
  });
});

