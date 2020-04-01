$(document).ready(function() {

var modal = document.getElementById("myModal");
var modalImg = document.getElementById("img01");
var captionText = document.getElementById("caption");
//img.onclick = function(){


$(".myImg").click(function(){
    var img=this
    modal.style.display = "block";
    modalImg.src = img.src;
    captionText.innerHTML = img.alt;
});
    

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function() { 
  modal.style.display = "none";
}


});




