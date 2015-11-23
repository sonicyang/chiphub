var GOAL = 3000;
var current_rally = 0;
var rally_person_count = 0;

$(document).ready(function(){
    $.get("/rally_digikey/", function(data){
        data = JSON.parse(data);
        current_rally = parseFloat(data[0]);
        rally_person_count = data[1];
        update_price();
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





