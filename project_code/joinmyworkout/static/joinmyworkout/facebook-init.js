window.fbAsyncInit = function() {
  FB.init({
    appId: '658628720985506',
    cookie: true,
    xfbml: true,
    version: 'v2.8'
  });
};

(function(d, s, id){
   var js, fjs = d.getElementsByTagName(s)[0];
   if (d.getElementById(id)) {return;}
   js = d.createElement(s); js.id = id;
   js.src = "//connect.facebook.net/en_US/sdk.js#xfbml=1&version=v2.8&appId=1247676591963389";
   fjs.parentNode.insertBefore(js, fjs);
 }(document, 'script', 'facebook-jssdk'));
