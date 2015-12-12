app.controller('chatroom-ctrl', function($scope, $http, $rootScope, $document) {
    $scope.infoing = false;
    $scope.families = [];
    $scope.comments = [];

    $http.get("/chatroom/top100/")
        .then(function(response){
            $scope.families = response.data;
        });

    $scope.show_info = function(family, chip){
        $scope.infoing = true;
        $scope.info = chip;
        $scope.info_family = family;
        $scope.price = chip.digikey.unit_price;
        $http.get("/chatroom/get_component_comments?pk=" + chip.id)
            .then(function(response){
                $scope.comments = response.data;
            });
    };

    $scope.hide_info = function(){
        $scope.infoing = false;
    };

    $document.on('keyup',function(evt) {
        if (evt.keyCode == 27) {
            $scope.hide_info();
            $scope.$apply()
        }
    });
});
