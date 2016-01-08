app.controller('order_info_ctrl', function($scope, $http, $rootScope, $document) {
    $scope.orders = [];
    $scope.invoice = false;
    $scope.editing_info = false;

    $scope.fee = 1.1;
    $scope.shipping_fee = 60;

    $http.get("/digikey/user_history")
        .then(function(response){
            response.data = response.data.reverse();

            for(uuid of response.data){
                $http.get("/digikey/order_info?UUID=" + uuid)
                    .then(function(response){
                        if(response.data["paid_date"] == "None"){
                            response.data["paid_date"] = "尚未付款"
                        }
                        if(response.data["paid_account"] == "None" || !response.data["paid_account"]){
                            response.data["paid_account"] = "尚未付款"
                        }
                        if(response.data["sent_date"] == "None"){
                            response.data["sent_date"] = "尚未寄送"
                        }
                        $scope.orders.push(response.data);
                    });
            }
        });

    $scope.show_info = function(order){
        $scope.invoice = true;
        $scope.info = order;
        $scope.chips = order.components;
        $scope.total_price = 0;
        for(c of order.components){
            $scope.total_price += c.quantity * c.unit_price;
        }
    };

    $scope.disableEditPaidInfoMode = function(){
        $("#info-paid-account").css("box-shadow", "");
        $("#info-paid-date").css("box-shadow", "");

        $scope.editing_info = false;
    }

    $scope.hide_info = function(){
        $scope.disableEditPaidInfoMode();
        $scope.invoice = false;
    };

    $scope.editPayment = function(order){
        $("#info-paid-account").css("box-shadow", "0 0 2px 0px #0000cc");
        $("#info-paid-date").css("box-shadow", "0 0 2px 0px #0000cc");

        $scope.editing_info = true;
        createPaidDatePicker();
    };

    $scope.sendPayment = function(order){
        var account = $("#info-paid-account").attr("value").replace(/\s/g, '');
        var date = new Date(getPaidDate());
        var month = date.getMonth() + 1;
        var day = date.getDate();
        if (!isNaN(month) && !isNaN(day)){
            $http.post("/digikey/pay", {"OID": order.uuid, "PACCOUNT": account, "PDAY": day, "PMONTH": month})
                .then(function(d){
                        $scope.disableEditPaidInfoMode();
                    }, function(d){
                        alert("儲存失敗");
                    });
        }else{
            alert("錯誤的日期格式")
        }
    };

    $document.on('keyup',function(evt) {
        if (evt.keyCode == 27) {
            $scope.hide_info();
            $scope.$apply()
        }
    });

    $('#order-info').bind("mousewheel DOMMouseScroll", function(e) {
        var scrollTo = null;
        if (e.type == 'mousewheel') {
            scrollTo = (e.originalEvent.wheelDelta * -1);
        } else if (e.type == 'DOMMouseScroll') {
            scrollTo = 1000 * e.originalEvent.detail;
        }

        if (scrollTo) {
            e.preventDefault();
            $(this).scrollTop(scrollTo + $(this).scrollTop());
        }
    });

    // avoid change line while pressing the enter key
    $("#info-paid-account").keydown(function(event){
        if(event.keyCode == 13){
            return false
        }
    });

    $("#info-paid-date").keydown(function(event){
        if(event.keyCode == 13){
            return false
        }
    });
});
function createPaidDatePicker(){
     $("#info-paid-date").datepicker();
}
function getPaidDate(){
     return $("#info-paid-date").attr("value");
}
