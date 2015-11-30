function changeAlertMsgForRWD(){
    $("#alert-message").css("left", function(){
        return $(window).width() / 2 - $(this).outerWidth() / 2;
    })
}

function alertWarning(type){
    alert_msg = $("#alert-message")
    alert_msg.text(type);
    changeAlertMsgForRWD();
    alert_msg.animate({top:"10px"}, 500);
}

function alertWarningClear(){
    alert_msg = $("#alert-message")
    changeAlertMsgForRWD();
    alert_msg.animate({top:"-100px"}, 500);
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

var order_dom_element = "\
        <div class=\"form-group order\">\
            <div class=\"col-md-7 order-item order-row\">\
                <div class=\"row\">\
                    <label class=\"col-xs-3 control-label order-item\" for=\"\">料號:</label>\
                    <div class=\"col-xs-8 order-item\">\
                        <input type=\"pd\" class=\"form-control pd\">\
                    </div>\
                </div>\
            </div>\
            <div class=\"col-md-5 order-item order-row\">\
                <div class=\"row\">\
                    <label class=\"col-xs-3 control-label order-item\" for=\"\">數量:</label>\
                    <div class=\"col-xs-3 order-item\">\
                        <input type=\"amounts\" class=\"form-control amounts\">\
                    </div>\
                    <label class=\"col-xs-3 control-label order-item\" for=\"\" >金額:</label>\
                    <label class=\"col-xs-3 control-label order-item price\" for=\"\" >-</label>\
                </div>\
            </div>\
        </div>\
    ";
var order_list = ""
function add_chip(){
    $("#chip-list").append(order_dom_element)
    $("#chip-list").append(order_dom_element)
    $("#chip-list").append(order_dom_element)
}

function update_price(data){
    var total = 0;
    $(".price").each(function(index){
        price = parseInt(data[index][1], 10) * data[index][2];
        $(this).text(price);
        total += price;
    })
    $('#total-price').text(total)
}
function cancel_form(){
    if(confirm("您尚未提交訂單，確定要離開?")){
        window.location.href = "/";
    }
}
function go_to_stage2(){
    $(".pd").prop("disabled", true);
    $(".amounts").prop("disabled", true);

    $("#order-button").hide()
    $("#confirm-button").hide()
    $("#cancel-button").hide()
    $("#submit-button").show()
    $("#modify-button").show()

}
function back_to_stage1(){
    $(".pd").prop("disabled", false);
    $(".amounts").prop("disabled", false);

    $("#order-button").show()
    $("#confirm-button").show()
    $("#cancel-button").show()
    $("#submit-button").hide()
    $("#modify-button").hide()

}
function arrange_order(){
    var pds = $(".pd")
    var amounts = $(".amounts")
    var orders = $(".order")
    order_list = "";
    for (var i = 0; i < pds.length; i ++){
        pd = $(pds[i]).attr("value")
        pd_amounts = $(amounts[i]).attr("value")
        if (pd !== "" && pd_amounts !== ""){
            order_list += $(pds[i]).attr("value")
            order_list += ":"
            order_list += $(amounts[i]).attr("value")
            order_list += ","
        }else{
            $(orders[i]).remove()
        }
    }
}
function confirm_price(){
    arrange_order()
    if (order_list !== ""){
        order_list = order_list.slice(0, -1)
        $(".loader").show()
        $.get("/price_digikey/",
            {order_list: order_list})
             .success(function(data){
                $(".loader").hide()
                update_price(JSON.parse(data));
                alertWarningClear();
                resetColor();
                go_to_stage2();
             })
             .error(function(jqXHR){
                 if (jqXHR.status == 400){
                    $(".loader").hide()
                    alertWarning("有不存在的料號、不可以1單位訂購的零件、沒有庫存的零件");
                    data = JSON.parse(jqXHR.responseText);
                    for(var i = 0; i < data.length; i++){
                        if(data[i][2] <= 0){
                            warningColor(i);
                        }
                    }

                }
             })
    }else{
        $("#chip-list").append(order_dom_element)
        alert("No Order!")
    }
}

function modify_form(){
    back_to_stage1();
}

function submit_form(){
    $.get("/order_digikey/",
        {order_list: order_list}
    )
    .success(function(){
        window.location.href = "/progress/";
    })
    $(".loader").show();
}
