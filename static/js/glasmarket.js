function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}

function confirmDelete(listingName){
  var r = confirm("are you sure you want to delete "+listingName);
  if (r == true){
    return true;
  }
  else {
    return false;
  }
}
function confirmLogout(){
  var r = confirm("are you sure you want to logout");
  if (r == true){
    return true;
  }
  else {
    return false;
  }
} 

function openAddForm(){
  document.getElementById("myDropForm").toggle("show");
}


// When the user scrolls the page, execute myFunction
window.onscroll = function() {topScroll()};

// Get the navbar
var navbar = document.getElementById("navbar");

// Get the offset position of the navbar
var sticky = navbar.offsetTop;

// Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
function topScroll() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky")
  } else {
    navbar.classList.remove("sticky");
  }
} 

