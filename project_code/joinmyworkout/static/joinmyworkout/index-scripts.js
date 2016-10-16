function checkLoginState() {
  console.log("status check.");
  FB.getLoginStatus(function(response) {
    statusChangeCallback(response);
  });
}

FB.getLoginStatus(function(response) {
  statusChangeCallback(response);
});


function statusChangeCallback(response) {
  console.log(response);
  if (response.status = "connected") {
    console.log("status: connected");
    console.log(response.authResponse.accessToken);
    location.href = "/search";
  } else {
    console.log("status: not connected");
  }
}
