// Login Form 1
$(document).ready(function(){
  $("#login_button").click(function(){
    $('#login_wrapper').fadeIn(700)

      return false; //To prevent browser appending a # on to the URL
  });

  $("#login_wrapper").click(function(){
    $('#login_wrapper').fadeOut(700)
  });
});

var app = angular.module('navbar', []);
app.controller('navbar-ctrl', function($scope, $http) {
     $scope.logined = false;

     $http.get("/islogin")
     .then(function(response) {
         if(response.status == 200){
             $scope.logined = true;
         }else if(response.status == 400){
             $scope.logined = false;
         }
     });

     $scope.login = function(){
        $('#login_wrapper').fadeIn(700)
     };
});

