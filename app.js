var firebase = require("firebase");

var config = {
    apiKey: "AIzaSyDeuYQudLLxNp99TohBZHQK5wIveC90wfc",
    authDomain: "test-e691e.firebaseapp.com",
    databaseURL: "https://test-e691e.firebaseio.com",
  };
  firebase.initializeApp(config);


function submit() {
    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var message = document.getElementById('message_form').value;
    // write to firebase
}

function inTouch() {
    location.replace("contact.html");
}

function viewLinkedIn() {
    location.replace("https://www.linkedin.com/in/dhriti-wasan-568ba6156");
}

function viewGithub() {
    location.replace("https://github.com/dhritiwasan14");
}

function viewFacebook() {
    location.replace("https://www.facebook.com/dhriti.wasan");
}

function viewInstagram() {
    location.replace("https://www.instagram.com/dritz1410/");
}