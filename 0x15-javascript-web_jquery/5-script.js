// Make sure that the DOM is loaded before running the script
$(document).ready(function() {
  // Then add a click event listener to the DIV#add_item element
  $('#add_item').click(function() {
    // Put a new <li> element with the text Item to the UL.my_list element
    $('ul.my_list').append('<li>Item</li>');
  });
});

