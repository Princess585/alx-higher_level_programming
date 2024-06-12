// Make sure the DOM is fully loaded before running the script
$(document).ready(function() {
  // Add a click event listener to the DIV#toggle_header element
  $('#toggle_header').click(function() {
    // Toggle the cls of the <header> element between 'red' and 'green'
    if ($('header').hasClass('red')) {
      $('header').removeClass('red').addClass('green');
    } else {
      $('header').removeClass('green').addClass('red');
    }
  });
});

