var data;
var order_html = "\
    <div class=\"order\">\
        <div class=\"container-fluid\">\
            <a class=\"order-info-link\" href=\"#\">link</a>\
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

var chip_html = "\
    <div class=\"row chip invoice-module\">\
        <div class=\"\">\
            <div class=\"col-md-6\">\
                <h3>CHIP</h3>\
                <div class=\"invoice-for part-number\">\
                </div>\
            </div>\
        </div>\
        <div class=\"\">\
            <div class=\"col-md-6\">\
                <h3>單價</h3>\
                <div class=\"invoice-for unit-price\">\
                </div>\
            </div>\
        </div>\
        <div class=\"\">\
            <div class=\"col-md-6\">\
                <h3>數量</h3>\
                <div class=\"invoice-for quantity\">\
                </div>\
            </div>\
        </div>\
        <div class=\"\">\
            <div class=\"col-md-6\">\
                <h3>總價 (單價X數量)</h3>\
                <div class=\"invoice-for chip-total-price\">\
                </div>\
            </div>\
        </div>\
    </div>\
"
var data_list = []
$.get("/user_history_digikey/", function(d){
    list = JSON.parse(d);
    list = list.reverse();
    $(document).ready(function(){
        order_list = $("#order-list")
        for (var i = 0; i < list.length; i ++){
            order_list.append(order_html);
        }
        counter = 0
        $('.order').each(function(index){
            var item = $(this)
            $.get("/order_info_digikey?UUID=" + list[index], function(d){
                data = JSON.parse(d)
                data_list[index] = data
                counter += 1
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
                item.find(".order-info-link").attr("index", index)

                if(counter == list.length){
                    addEventForLinks()
                }
            })
        })
        //$("label[type=shipping_address]").each(function(index){
            //console.log(data[index]['shipping_address'])
        //})
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
    })

    $(document).on('keyup',function(evt) {
        if (evt.keyCode == 27) {
            $("#order-info").hide();
        }
    });

    $("#close-order-info").click(function(){
            $("#order-info").hide();
    })

})
function addEventForLinks(){
    $(".order-info-link").click(function(e){
        $(".chip").remove()
        var ind = $(this).attr("index")
        $("#info-shipping-address").text(data_list[ind]["shipping_address"])
        $("#info-sent-date").text(data_list[ind]["sent_date"])
        $("#info-net").text(data_list[ind]["net"])
        $("#info-paid-date").text(data_list[ind]["paid_date"])
        $("#info-paid-account").text(data_list[ind]["paid_account"])

        for (var i = 0; i < data_list[ind]['components'].length; i ++){
            $("#chip-list").append(chip_html)
        }
        $("#chip-list .chip").each(function(){
            var chip = $(this)
            var comp = data_list[ind]['components'][chip.index()]
            chip.find(".part-number").text(comp['part_number'])
            chip.find(".unit-price").text(comp['unit_price'])
            chip.find(".quantity").text(comp['quantity'])
            chip.find(".chip-total-price").text(comp['quantity'] * comp['unit_price'])
        })
        $("#order-info").show()
    })

}
