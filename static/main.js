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
var r = document.querySelector(':root');
if (localStorage.getItem("theme") == false || localStorage.getItem("theme") == "false"){
  console.log(1)
  r.style.setProperty('--bg', '#FDEFF4');
  r.style.setProperty('--dark', 'white');
  r.style.setProperty('--pText', 'black');
  r.style.setProperty('--subject', '#1C6DD0' )
}else if(localStorage.getItem("theme") == true || localStorage.getItem("theme") == "true"){
  
}
