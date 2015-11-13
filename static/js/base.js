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
        $("#login_button_wrapper").hide()
          $("#logout_button_wrapper").show()
          $("#profile_button_wrapper").show()
      },
      400: function(){
        $("#login_button_wrapper").show()
          $("#logout_button_wrapper").hide()
          $("#profile_button_wrapper").hide()

      }
    }
  })
});

