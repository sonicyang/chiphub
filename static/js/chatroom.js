app.controller('chatroom-ctrl', function($scope, $http, $rootScope, $document) {
    $scope.infoing = false;
    $scope.families = [];
    $scope.comments = [];
    $scope.comment_text = "";
    $scope.max_comment_length = 300;
    $scope.remaining_char = $scope.max_comment_length;

    $http.get("/chatroom/top100")
        .then(function(response){
            $scope.families = response.data;

            console.log($scope.families);
        });

    $scope.search = function(text){
        if(text){
            console.log(text);
            $http.get("/chatroom/search?s=" + text)
                .then(function(response){
                    $scope.families = response.data;
                    console.log($scope.families);
                });
        }else{
            $http.get("/chatroom/top100")
                .then(function(response){
                    $scope.families = response.data;
                });
        }
    };

    $scope.submitComment = function(chip){
        $http.post("/chatroom/add_component_comment", {"pk": chip.id, "content": $scope.comment_text})
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
        $scope.comments = null;
        $http.get("/chatroom/get_component_comments?pk=" + chip.id)
            .then(function(response){
                $scope.comments = response.data;
            });
    };

    $scope.rank_comment = function(comment, up){
        var up = up ? "True": "False"
        $http.get("/chatroom/rank_comment?pk=" + comment.id + "&up=" + up)
         .then(function(response){
             comment.rank += parseInt(response.data)
         });
    }
    $scope.rank_entry = function(chip, up){
        var up = up ? "True": "False"
        $http.get("/chatroom/rank_entry?pk=" + chip.id + "&up=" + up)
         .then(function(response){
             chip.rank += parseInt(response.data)
         });
    }
    $scope.hide_info = function(){
        $scope.infoing = false;
    };
    $scope.onInputComment = function(){
        $scope.remaining_char = $scope.max_comment_length - $scope.comment_text.length;
    }
    $document.on('keyup',function(evt) {
        if (evt.keyCode == 27) {
            $scope.hide_info();
            $scope.$apply()
        }
    });

    $("part-number").on('keypress',function(evt) {
        if (evt.keyCode == 13) {
			$scope.search(stext);
        }
    });
});
