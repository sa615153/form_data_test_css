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


window.onload = function(){
alert("js recognized")
//var button = document.querySelector("button");
alert("alert2");
var p = document.getElementById("p");
alert(p)
p.innerHTML = "123";
alert("alert3");
button=document.getElementById("btn");
alert("alert4");
console.log(button);
alert("alert5");
button.addEventListener("click", changeBg);
alert("alert6");
console.log(button);
alert("alert7");
};