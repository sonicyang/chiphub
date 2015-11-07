$(document).ready(function(){
	$("#login_button").click(function(){
        $('#login_wrapper').fadeIn(700)

        return false; //To prevent browser appending a # on to the URL
	});

	$("#login_wrapper").click(function(){
        $('#login_wrapper').fadeOut(700)
	});
});

