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
const db = firebase.database();

function signup() {
    full_name = document.getElementById("full_name").value;
    email = document.getElementById("email").value;
    password = document.getElementById("password").value;
    
    //validate input fields
    if(validate_email == false || validate_password == false) {
        alert('Email or password cannot be used')
        return
    }

    //authentication
    auth.createUserWithEmailAndPassword(email, password)
.then(function() {
    var user = auth.currentUser

    var db_ref = db.ref()

    var user_data = {
        email : email, full_name : full_name, last_login : Date.now()
    }

    db_ref.child('user/' + user.uid).set(user_data)

    alert('User Created!!!')
    window.location.assign("index.html")
})
.catch(function(error) {
    //firebase will use this to alert if its an error
    var error_code = error.code
    var error_message = error.message

    alert(error_message)
})
}

function validate_email(email) {
    expression = /^[^@]+@\w+(\.\w+)+\w$/
    if(expression.test(email) == true) {
        return true
    } else {
        //email is not good
        return false
    }
}

function validate_password(password){
    if(password < 6) {
        return false
    } else {
        return true
    }
}

function validate_field(field) {
    if (field == null) {
        return false
    }

    if(field.length <= 0) {
        return false 
    } else {
        return true
    }
}

//login form 
function login() {
    email = document.getElementById("email").value;
    password = document.getElementById("password").value;

    //validate input fields
    if(validate_email == false || validate_password == false) {
        alert('Email or password cannot be used')
        return
    }

    auth.signInWithEmailAndPassword(email, password)
    .then(function(){
        var user = auth.currentUser

        var db_ref = db.ref()

        var user_data = {
        last_login : Date.now()
    }

    db_ref.child('user/' + user.uid).update(user_data)

    alert('User logged In')
    window.location.assign("homepage.html")
    })
    .catch(function(error) {
        //firebase will use this to alert if its an error
        var error_code = error.code
        var error_message = error.message
    
        alert(error_message)
    })
}