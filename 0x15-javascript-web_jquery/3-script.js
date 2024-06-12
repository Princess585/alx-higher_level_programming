// Ensure the DOM is fully loaded before running the script
$(document).ready(function() {
  // Add a click event listener to the DIV#red_header element
  $('#red_header').click(function() {
    // Add the class 'red' to the <header> element
    $('header').addClass('red');
  });
});

