app.controller('chatroom-ctrl', function($scope, $http, $rootScope, $document) {
    $scope.infoing = false;
    $scope.families = [];
    $scope.comments = [];
    $scope.comment_text = "";

    $http.get("/chatroom/top100/")
        .then(function(response){
            $scope.families = response.data;
        });

    $scope.submitComment= function(chip){
        //XXX: Use Post
        $http.get("/chatroom/add_component_comment?pk=" + chip.id + "&content=" + $scope.comment_text)
            .then(function(response){
                $scope.comment_text = "";
                $http.get("/chatroom/get_component_comments?pk=" + chip.id)
                    .then(function(response){
                        $scope.comments = response.data;
                    });
            });
    };

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
