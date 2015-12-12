$('#myCarousel').carousel({
    interval: 200
});

app.controller('progress', function($scope, $http, $window, $rootScope) {
    $http.get("/digikey/rally/")
        .then(function(response) {
            $scope.current_accumulated = parseFloat(response.data[0]);
            $scope.current_person_count = parseFloat(response.data[1]);
            $scope.current_percent = parseFloat(response.data[0] / 3000 * 100).toFixed(2);

            //XXX: use ngAnimate
            percent = parseFloat(response.data[0] / 3000 * 100);
            $('#progress').animate({width: (percent + "%")}, 750);

        });

        $scope.go_order = function(){
            $http.get("/islogin")
                .then(function(response) {
                        $window.location.href = '/order';
                      },function(response){
                        $rootScope.$broadcast("showLogin");
                      });
        };
});

app.controller('group_history', function($scope, $http) {
    $scope.groups = [];

    $http.get("/digikey/groups/")
        .then(function(response) {
            response.data = response.data.reverse();

            for(uuid of response.data){
                $http.get("/digikey/group_info?UUID=" + uuid).then(function(response){
                    if(response.data["date"] == "None"){
                        response.data["date"] = "已成單，正在訂購"
                    }
                    $scope.groups.push(response.data);
                });
            }
        });
});
