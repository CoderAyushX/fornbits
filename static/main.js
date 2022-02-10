// navbar
function show() {
    document.getElementById("navItems").classList.toggle("show");

}
//nav for mobile
const list = document.querySelectorAll('.list');
function activeLink() {
  list.forEach((item)=> item.classList.remove('active'));
  this.classList.add('active');
}
list.forEach((item)=> item.addEventListener( 'click', activeLink ))

function delay (URL) {
  setTimeout( function() { window.location = URL }, 100 );
}
window.addEventListener("load", function() {
  document.getElementById("loader").style.display = "none";
  document.getElementById("body").style.opacity = "1";
  document.getElementById("footer").style.display = "block";
});

