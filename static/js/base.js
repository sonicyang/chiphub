$(document).ready(function(){
	$("#login_button").click(function(){
        $('#login_wrapper').show(700)

        return false; //To prevent browser appending a # on to the URL
	});

	$("#login_wrapper").click(function(){
        $('#login_wrapper').hide(700)
	});
});

