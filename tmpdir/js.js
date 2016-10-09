// JavaScript demonstration
var changeBg = function (event) {
    console.log("method called");
    var me = event.target;
    square = document.getElementById("square");
    square.style.backgroundColor = "#ffaa44";
    me.setAttribute("disabled", "disabled");
    setTimeout(function () { clearDemo(me) }, 2000);
}

function clearDemo(button) {
    var square = document.getElementById("square");
    square.style.backgroundColor = "transparent";
    button.removeAttribute("disabled");
}

//window.onload = function(){
alert("js recognized")
//var button = document.querySelector("button");
alert("alert2");
var p = document.getElementById("pisp");
alert(p)
p.innerHTML = "123";

button=document.getElementById("btn");

console.log(button);

button.addEventListener("click", changeBg);

console.log(button);

//};