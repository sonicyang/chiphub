
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

    $scope.item = [{pn: "", quantity: ""}];
    $scope.item_count = 1;
    $scope.stage = 1;
    $scope.loading = false;

    $scope.increase_item_count = function(){
        $scope.item_count += 3;
        for(var i = 0; i < 3; i ++){
            $scope.item.push({pn: "", quantity: ""})
        }
    };

    $scope.go_to_stage = function(num){
        $scope.stage = num;
    };

    $scope.arrange_order = function(){
        var input_error = false;
        order_list = "";

        for(item of $scope.item){
            var quantity = parseInt(item.quantity);
            var pn = item.pn.replace(/\s/g, "");
            if (pn){
                order_list += item.pn + ":" + item.quantity + ",";
                if(isNaN(quantity)){
                    input_error = true;
                }
            }
        }
        if(input_error){
            order_list = "";
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

        var order_list = $scope.arrange_order();
        if(order_list != ""){
            $scope.loading = true;
            $http.post("/digikey/price/", {"order_list": order_list})
                .then(function(response){
                        console.log(200);
                        var total = 0;

                        response.data.forEach(function(element, index){
                            $scope.item[index].unit_price = parseInt(element["unit_price"], 10)
                            $scope.item[index].price = parseInt(element["unit_price"], 10) * element["quantity"]
                            total += $scope.item[index].price;
                        });

                        $scope.fee = Math.ceil(total * $scope.fee_rate);
                        $scope.sum_price = total + $scope.fee + $scope.shipping_fee;

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
            var new_item_list = [];
            var new_item_count = 0;
            for(item of $scope.item){
                if(item.pn){
                    var new_item = {pn: "", quantity: ""};
                    if(!isNaN(parseInt(item.quantity))){
                        new_item.quantity = item.quantity;
                    }
                    new_item.pn = item.pn;
                    new_item_list.push(new_item);
                    new_item_count += 1;
                }
            }
            if(new_item_count < 1){
                $scope.item_count = 1;
                $scope.item = [{pn: "", quantity: ""}]
            }else{
                $scope.item_count = new_item_count;
                $scope.item = new_item_list;
            }

            alertWarning("未輸入訂單或輸入了錯誤的零件數量!")
        }
    };

    $scope.submit_form = function(){
        $scope.loading = true;
        $http.post("/digikey/order", {"order_list": $scope.arrange_order()})
            .then(function(response){
                if(response.status == 200){
                    $scope.stage = 4
                $scope.loading = false;
                    //window.location.href = "/progress/";
                }
            });
    };
});

$(window).resize(function(){
    changeAlertMsgForRWD();
})
