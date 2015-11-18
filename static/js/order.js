function add_chip(){
    var content = "<div class=\"form-group order\">\
        <label class=\"col-md-2 control-label\" for=\"\">料號:</label>\
            <div class=\"col-md-4\">\
                <input type=\"pd\" class=\"form-control pd\">\
            </div>\
            <label class=\"col-md-2 control-label\" for=\"\">數量:</label>\
            <div class=\"col-md-4\">\
                <input type=\"amounts\" class=\"form-control amounts\">\
            </div>\
        </div>"
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
