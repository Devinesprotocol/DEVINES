let pantheon = null
let entity = null


function selectPantheon(name){

pantheon = name

localStorage.setItem("pantheon",name)

window.location = "/pantheon.html"

}


function selectEntity(name){

entity = name

localStorage.setItem("entity",name)

window.location = "/chat.html"

}


async function sendMessage(){

const message = document.getElementById("message").value

const response = await fetch("/chat",{

method:"POST",

headers:{"Content-Type":"application/json"},

body:JSON.stringify({

pantheon:localStorage.getItem("pantheon"),

entity:localStorage.getItem("entity"),

message:message

})

})

const data = await response.json()

const chat = document.getElementById("chat-window")

chat.innerHTML += "<p><b>You:</b> "+message+"</p>"

chat.innerHTML += "<p><b>"+data.entity+":</b> "+data.response+"</p>"

}
