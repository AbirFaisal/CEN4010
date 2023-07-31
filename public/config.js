// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
    apiKey: "AIzaSyDg4dfnbxFCNCv5nNNEDpGGz0czKjyPobU",
    authDomain: "cen4010-group-6.firebaseapp.com",
    projectId: "cen4010-group-6",
    storageBucket: "cen4010-group-6.appspot.com",
    messagingSenderId: "338954220916",
    appId: "1:338954220916:web:b5785539e012e60215e821",
    measurementId: "G-DVK23P66SP"
  };


firebase.initializeApp(firebaseConfig);

const auth = firebase.auth();

function login() {
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    auth.signInWithEmailAndPassword(email, password).then (cred => {
        alert(cred.user.email + " has logged in")
    })
}

function signup() {
    email = document.getElementById("email").value;
    password = document.getElementById("Password").value;
    auth.createUserWithEmailAndPassword(email, password).then (cred => {
        alert(cred.user.email + " has signed up")
    })
}
