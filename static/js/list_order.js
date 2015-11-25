var data;
var order_html = "\
    <div class=\"order\">\
        <div class=\"container-fluid\">\
            <div class=\"row\">\
                <div class=\"col-md-5\">\
                    <h2 class=\"order-date\" type=\"date\">2015/12/31</h2>\
                </div>\
                <div class=\"col-md-7\">\
                    <h2 class=\"order-price\" type=\"net\">asdasd</h4>\
                </div>\
            </div>\
            <div class=\"row\">\
                <div class=\"col-md-4 info-item\">\
                    <label class=\"control-label\">\
                        寄送日期：\
                    </label>\
                    <label class=\"control-label output sent\" type=\"sent_date\"></label>\
                </div>\
                <div class=\"col-md-8 info-item\">\
                    <label class=\"control-label\">\
                        寄送地址：\
                    </label>\
                    <label class=\"control-label output sent\" type=\"shipping_address\"></label>\
                </div>\
            </div>\
            <div class=\"row\">\
                <div class=\"col-md-4 info-item\">\
                    <label class=\"control-label\">\
                        匯款日期：\
                    </label>\
                    <label class=\"control-label output paid\" type=\"paid_date\"></label>\
                </div>\
                <div class=\"col-md-8 info-item\">\
                    <label class=\"control-label\">\
                        匯款帳戶：\
                    </label>\
                    <label class=\"control-label output paid\" type=\"paid_account\"></label>\
                </div>\
            </div>\
        </div>\
    </div>\
    <hr />\
";

$.get("/user_history_digikey/", function(d){
    list = JSON.parse(d);
    list = list.reverse();
    $(document).ready(function(){
        order_list = $("#order-list")
        for (var i = 0; i < list.length; i ++){
            order_list.append(order_html);
        }
        $('.order').each(function(index){
            var item = $(this)
            $.get("/order_info_digikey?UUID=" + list[index], function(d){
                data = JSON.parse(d)

                item.find('.order-date').each(function(){
                    var type = $(this).attr("type");
                    var text = data[type];
                    $(this).text(text);
                })

                item.find('.order-price').each(function(){
                    var type = $(this).attr("type");
                    var text = data[type];
                    text = '$ ' + text;
                    $(this).text(text);
                })

                item.find(".sent").each(function(){
                    var type = $(this).attr("type");
                    var text = data[type];
                    if (!text || text == "None"){
                        text = "尚未寄送";
                    }
                    $(this).text(text);
                })

                item.find(".paid").each(function(){
                    var type = $(this).attr("type");
                    var text = data[type];
                    if (!text || text == "None"){
                        text = "尚未付款";
                    }
                    $(this).text(text);
                })
            })
        })
        //$("label[type=shipping_address]").each(function(index){
            //console.log(data[index]['shipping_address'])
        //})
    })
})
