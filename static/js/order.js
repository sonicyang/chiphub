
//XXX: Purge JQuery
function changeAlertMsgForRWD(){
    $("#alert-message").css("left", function(){
        return $(window).width() / 2 - $(this).outerWidth() / 2;
    })
}

function alertWarning(type){
    alert_msg = $("#alert-message")
    alert_msg.text(type);
    changeAlertMsgForRWD();
    alert_msg.animate({top:"70px"}, 500);
}

function alertWarningClear(){
    alert_msg = $("#alert-message")
    changeAlertMsgForRWD();
    alert_msg.animate({top:"-50px"}, 500);
}

function warningColor(no){
    $($("input[type=\"pd\"]")[no]).css("border-color", "#ff0000");
    $($("input[type=\"pd\"]")[no]).css("box-shadow", "0 0 5px rgba(255, 000, 0, 0.4)");
}

function normalColor(no){
    $($("input[type=\"pd\"]"))[no].css("border-color", "");
    $($("input[type=\"pd\"]"))[no].css("box-shadow", "");
}
function resetColor(){
    $("input[type=\"pd\"]").css("border-color", "");
    $("input[type=\"pd\"]").css("box-shadow", "");
}

app.controller('order_main', function($scope, $http) {
    $scope.getNumber = function(num) {
        return new Array(num);
    };

    $scope.shipping_fee = 60
    $scope.fee_rate = 0.1


    $scope.item = [];
    $scope.item_count = 1;
    $scope.stage = 1;
    $scope.loading = false;

    $scope.increase_item_count = function(){
        $scope.item_count += 3;
    };

    $scope.go_to_stage = function(num){
        $scope.stage = num;
    };

    $scope.arrange_order = function(){
        order_list = "";

        for(item of $scope.item){
            order_list += item.pn + ":" + item.quantity + ",";
        }
        if(order_list != ""){
            order_list = order_list.slice(0, -1)
        }

        $scope.item_count = $scope.item.length;

        return order_list;
    }

    $scope.cancel_form = function(){
        if(confirm("您尚未提交訂單，確定要離開?")){
            window.location.href = "/";
        }
    };

    $scope.confirm_price = function(){
        $scope.loading = true;

        var order_list = $scope.arrange_order();
        if(order_list != ""){
            $http.get("/digikey/price/?order_list=" + order_list)
                .then(function(response){
                        console.log(200);
                        var total = 0;

                        response.data.forEach(function(element, index){
                            $scope.item[index].unit_price = parseInt(element["unit_price"], 10)
                            $scope.item[index].price = parseInt(element["unit_price"], 10) * element["quantity"]
                            total += $scope.item[index].price;
                        });

                        $scope.sum_price = total;
                        $scope.fee = Math.ceil(total * $scope.fee_rate);

                        alertWarningClear();
                        resetColor();
                        $scope.stage = 2;

                        $scope.loading = false;
                    }, function(response){
                        if(response.status == 400){
                            console.log(400);
                            alertWarning("有不存在的料號、不可以1單位訂購的零件、沒有庫存的零件");
                            response.data.forEach(function(element, index){
                                if(element["unit_price"] <= 0){
                                    warningColor(index);
                                }
                            });
                        }else if(response.status == 500){
                            alertWarning("我們出錯了，請再試一次");
                        }

                        $scope.loading = false;
                    });
        }else{
            $scope.item_count = 1;
            alertWarning("尚未輸入任何訂單!")
        }
    };

    $scope.submit_form = function(){
        $scope.loading = true;
        $http.get("/digikey/order?order_list=" + $scope.arrange_order())
            .then(function(response){
                if(response.status == 200){
                    $scope.stage = 4
                    //window.location.href = "/progress/";
                }
            });
    };
});

$(window).resize(function(){
    changeAlertMsgForRWD();
})
