function onSignIn(googleUser) {
    var profile = googleUser.getBasicProfile();

    let params = {};
    params.username = profile.getName();
    params.email = profile.getEmail();
    params.imageUrl = profile.getImageUrl();
    params.signInType = 'google';
    post("/login/", params, function(result){
        console.log(result);
    });
}


function signOut() {
    var auth2 = gapi.auth2.getAuthInstance();
    auth2.signOut().then(function () {
      console.log('User signed out.');
    });
}