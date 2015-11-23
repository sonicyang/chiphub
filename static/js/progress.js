CountDownTimer('12/20/2014 10:1 AM', 'countdown');
CountDownTimer('12/20/2014 10:1 AM', 'newcountdown');
var GOAL = 3000;
var current_rally = 0;
var rally_person_count = 0;

$(document).ready(function(){
    $.get("http://127.0.0.1:8000/rally_digikey", function(data){
        data = JSON.parse(data);
        current_rally = parseFloat(data[0]);
        rally_person_count = data[1];
        update_price();
    })
})

function CountDownTimer(dt, id)
{
	var end = new Date(dt);

	var _second = 1000;
	var _minute = _second * 60;
	var _hour = _minute * 60;
	var _day = _hour * 24;
	var timer;

	function showRemaining() {
		var now = new Date();
		var distance = end - now;
		if (distance < 0) {

			clearInterval(timer);

			return;
		}
		var days = Math.floor(distance / _day);
		var hours = Math.floor((distance % _day) / _hour);
		var minutes = Math.floor((distance % _hour) / _minute);
		var seconds = Math.floor((distance % _minute) / _second);

		document.getElementById(id).innerHTML = days /*+ ' days'*/;
		//document.getElementById(id).innerHTML += hours + 'hrs ';
		//document.getElementById(id).innerHTML += minutes + 'mins ';
		//document.getElementById(id).innerHTML += seconds + 'secs';
	}

	timer = setInterval(showRemaining, 1000);
}

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





