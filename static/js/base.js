// Login Form 1
$(document).ready(function(){
  $("#login_button").click(function(){
    $('#login_wrapper').fadeIn(700)

      return false; //To prevent browser appending a # on to the URL
  });

  $("#login_wrapper").click(function(){
    $('#login_wrapper').fadeOut(700)
  });

  $.ajax({
    url: "/islogin",
    statusCode: {
      200: function(){
        $("#login_button_wrapper").fadeOut(350)
          $("#logout_button_wrapper").fadeIn(350)
          $("#profile_button_wrapper").fadeIn(350)
      },
      400: function(){
        $("#login_button_wrapper").fadeIn(350)
          $("#logout_button_wrapper").fadeOut(350)
          $("#profile_button_wrapper").fadeOut(350)

      }
    }
  })
});

