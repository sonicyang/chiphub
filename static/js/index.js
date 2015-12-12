var GOAL = 3000;
var current_rally = 0;
var rally_person_count = 0;

var data;
var order_html = "\
  <div class=\"row-list\">\
	  <input type=\"radio\" name=\"expand\">\
    <span class=\"cell-list primary order-date\" data-label=\"serial-num\" type=\"date\">2015-10-D-RC-103324</span>\
    <span class=\"cell-list order-price\" data-label=\"sum\" type=\"total\">NT$ 4500</span>\
    <span class=\"cell-list order-person\" data-label=\"person\" type=\"person\">8</span>\
  </div>\
";

$(document).ready(function(){
    $.get("/digikey/rally/", function(data){
        data = JSON.parse(data);
        current_rally = parseFloat(data[0]);
        rally_person_count = data[1];
        update_price();
    })
    $.ajax({
      url: "/islogin",
      statusCode: {
        200: function(){
            $("#list").fadeIn(350)
            $("#order").fadeIn(350)
        },
        400: function(){
            $("#list").fadeOut(350)
            $("#order").fadeOut(350)
        }
      }
    })
    $.get("/digikey/groups/", function(d){
        list = JSON.parse(d);
        list = list.reverse();
        $(document).ready(function(){
            order_list = $("#table-list")
            for (var i = 0; i < list.length; i ++){
                order_list.append(order_html);
            }
            $('.row-list').each(function(index){
                if(index==0){
                     return;
                }
                var item = $(this)
                $.get("/digikey/group_info?UUID=" + list[index - 1], function(d){
                    data = JSON.parse(d)

                    item.find(".order-date").each(function(){
                        var type = $(this).attr("type");
                        var text = data[type];
                        if (!text || text == "None"){
                            text = "尚未下訂";
                        }
                        $(this).text(text);
                    })

                    item.find('.order-price').each(function(){
                        var type = $(this).attr("type");
                        var text = data[type];
                        text = '$ ' + text;
                        $(this).text(text);
                    })

                    item.find('.order-person').each(function(){
                        var type = $(this).attr("type");
                        var text = data[type];
                        $(this).text(text);
                    })

                })
            })
            //$("label[type=shipping_address]").each(function(index){
                //console.log(data[index]['shipping_address'])
            //})
        })
    })
})

function update_price(){
    document.getElementById("funds-count").innerHTML = rally_person_count;

    var percent = current_rally / GOAL * 100;

    $('#progress').animate({
        width: (percent + "%")
    }, 750);
    $("#progress").css("width", percent + '%');
    $("#funds-raised").text('$' + current_rally)
    $("#funds-raised-percent").text(percent.toFixed(2) + '%')
    }

    /////////////////////////////////////////////////////////////  select section in main page */
    $("nav ul li").click(function(){
      var xcoord = $(this).data("xcoord");

      $("nav div").stop().animate({marginLeft:xcoord}, 500, "easeInOutExpo");
      $(this).addClass("active");
      $("nav ul li").not(this).removeClass("active");

    });
