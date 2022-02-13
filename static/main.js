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
  r.style.setProperty('--bg', '#F5F5F5');
  r.style.setProperty('--dark', 'white');
  r.style.setProperty('--pText', 'black');
  r.style.setProperty('--subject', '#1C6DD0' )
  document.getElementById("blogpost").style.boxShadow = "rgba(0, 0, 0, 0.1) 0px 4px 6px -1px, rgba(0, 0, 0, 0.06) 0px 2px 4px -1px";
  document.querySelector(".content").style.boxShadow = "rgba(50, 50, 93, 0.25) 0px 2px 5px -1px, rgba(0, 0, 0, 0.3) 0px 1px 3px -1px";
}else if(localStorage.getItem("theme") == true || localStorage.getItem("theme") == "true"){
  document.getElementById("blogpost").style.boxShadow = "none";
  document.querySelector(".content").style.boxShadow = "rgba(0, 0, 0, 0.19) 0px 10px 20px, rgba(0, 0, 0, 0.23) 0px 6px 6px";
}
