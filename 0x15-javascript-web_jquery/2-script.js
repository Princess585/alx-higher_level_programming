// Ensure the DOM is fully loaded before running the script
$(document).ready(function() {
  // Add a click event listener to the DIV#red_header element
  $('#red_header').click(function() {
    // Change the text color of the <header> element to red (#FF0000)
    $('header').css('color', '#FF0000');
  });
});

