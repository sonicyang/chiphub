
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
        $.get("/price_digikey/",
            {order_list: order_list})
             .success(function(data){
                update_price(JSON.parse(data))
                go_to_stage2();

             })
             .error(function(jqXHR){
                 if (jqXHR.status == 400){
                     alert("Chip not existed or no price!");
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
}
