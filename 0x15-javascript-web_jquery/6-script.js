// Make sure that the DOM is loaded fully before running the script
$(document).ready(function() {
  // Then add a click event listner to the DIV#update_header element
  $('#update_header').click(function() {
    // Make an update to the text of the <header> elmnt to New Head!!!"
    $('header').text('New Header!!!');
  });
});

