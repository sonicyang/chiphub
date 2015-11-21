function add_chip(){
    var content = "\
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
                        <label class=\"col-xs-3 control-label order-item price\" for=\"\" >金額:</label>\
                        <label class=\"col-xs-3 control-label order-item\" for=\"\" >-</label>\
                    </div>\
                </div>\
            </div>\
    "
    $("#chip-list").append(content)
    $("#chip-list").append(content)
    $("#chip-list").append(content)
}
function submit_form(){
    var pds = $(".pd")
    var amounts = $(".amounts")
    var order_list = ""
    for (var i = 0; i < pds.length; i ++){
        pd = $(pds[i]).attr("value")
        pd_amounts = $(amounts[i]).attr("value")
        if (pd !== "" && pd_amounts !== ""){
            order_list += $(pds[i]).attr("value")
            order_list += ":"
            order_list += $(amounts[i]).attr("value")
            order_list += ","
        }
    }
    if (order_list !== ""){
        order_list = order_list.slice(0, -1)
        $.get("/order_digikey/",
            {order_list: order_list}
        )
        console.log(order_list)
    }
}
