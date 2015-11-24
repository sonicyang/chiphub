var data;
var order_html = "\
    <div class=\"order\">\
        <div class=\"container-fluid\">\
            <h2 class=\"order-time\" type=\"date\">2015/12/31</h2>\
            <div class=\"row\">\
                <div class=\"col-md-4 info-item\">\
                    <label class=\"control-label\">\
                        寄出日期:\
                    </label>\
                    <label class=\"control-label output\" type=\"sent_date\"></label>\
                </div>\
                <div class=\"col-md-8 info-item\">\
                    <label class=\"control-label\">\
                        寄送地址:\
                    </label>\
                    <label class=\"control-label output\" type=\"shipping_address\"></label>\
                </div>\
            </div>\
            <div class=\"row\">\
                <div class=\"col-md-4 info-item\">\
                    <label class=\"control-label\">\
                        付款日期:\
                    </label>\
                    <label class=\"control-label output\" type=\"paid_date\"></label>\
                </div>\
                <div class=\"col-md-8 info-item\">\
                    <label class=\"control-label\">\
                        匯款帳戶:\
                    </label>\
                    <label class=\"control-label output\" type=\"paid_account\"></label>\
                </div>\
            </div>\
        </div>\
    </div>\
";
$.get("/list_digikey/", function(d){
    data = JSON.parse(d);

    $(document).ready(function(){
        order_list = $("#order-list")
        for (var i = 0; i < data.length; i ++){
            order_list.append(order_html);
        }
        $('.order').each(function(index){
            $(this).find('h2').each(function(){
                var type = $(this).attr("type");
                var text = data[index][type];
                if (!text){
                    text = "尚未付款";
                }
                $(this).text(text);
            })

            $(this).find(".output").each(function(){
                var type = $(this).attr("type");
                var text = data[index][type];
                if (!text){
                    text = "尚未付款";
                }
                $(this).text(text);
            })
        })
        //$("label[type=shipping_address]").each(function(index){
            //console.log(data[index]['shipping_address'])
        //})
    })
})
