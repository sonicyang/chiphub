var app = angular.module('base', ['ngAnimate']).config(function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});

app.controller('base-ctrl', function($scope, $http) {
     $scope.logined = false;
     $scope.login_wrapper = false;

     $http.get("/islogin")
        .then(function(response) {
                $scope.logined = true;
            },function(response){
                $scope.logined = false;
            });

     $scope.login = function(){
         $scope.login_wrapper = true;

         return false;
     };

     $scope.$on('showLogin', function(event) {
         $scope.login_wrapper = true;

         return false;
     })

     $scope.exit_login = function(){
         $scope.login_wrapper = false;

         return false;
     };
});

