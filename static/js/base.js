var app = angular.module('base', ['ngAnimate']);
app.controller('base-ctrl', function($scope, $http) {
     $scope.logined = false;
     $scope.login_wrapper = false;

     $http.get("/islogin")
     .then(function(response) {
         if(response.status == 200){
             $scope.logined = true;
         }else if(response.status == 400){
             $scope.logined = false;
         }
     });

     $scope.login = function(){
         $scope.login_wrapper = true;
     };

     $scope.exit_login = function(){
         $scope.login_wrapper = false;
     };
});

