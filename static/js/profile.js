
function validateNotEmpty(text){
    var re = /\s/g;
    if (text.replace(re, "") === ""){
        return false;
    }
    return true;
}

function validateEmail(email) {
    var re = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i;
    return re.test(email);
}

function validatePhone(phone){
    var re = /\s/g;
    if(isNaN(parseInt(phone, 10))){
        return false;
    }
    if(phone !== phone.replace(re, "")){
        return false;
    }
    if(phone.length < 9 || phone.length > 10){
        return false;
    }
    return true;
}

tab = "ABCDEFGHJKLMNPQRSTUVXYWZIO"
A1 = new Array (1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3 );
A2 = new Array (0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5 );
Mx = new Array (9,8,7,6,5,4,3,2,1,1);
function validateID(id) {

    if (id.length != 10) return false;
    var i = tab.indexOf(id.charAt(0));
    if (i == -1) return false;
    var sum = A1[i] + A2[i]*9;

    for (i = 1; i < 10; i++) {
        var v = parseInt(id.charAt(i));
        if (isNaN(v)) return false;
        sum = sum + v * Mx[i];
    }
    if (sum % 10 != 0) return false;
    return true;
}

function chooseValidateMethod(type){
    var method = "";
    switch(type){
        case "email":
            method = validateEmail;
            break;
        case "phone":
            method = validatePhone;
            break;
        case "id":
            method = validateID;
            break;
        default:
            method = validateNotEmpty;
    }
    return method;
}

function alertWarning(type){
    alert_msg = $("#alert-message")
    alert_msg.text(type + " 不合法！");
    changeAlertMsgForRWD();
    alert_msg.animate({top:"70px"}, 500);
}
function warningColor(input_type){
    $("input[type=\"" + input_type + "\"]").css("border-color", "#ff0000");
    $("input[type=\"" + input_type + "\"]").css("box-shadow", "0 0 5px rgba(255, 000, 0, 0.4)");
}

function normalColor(input_type){
    $("input[type=\"" + input_type + "\"]").css("border-color", "");
    $("input[type=\"" + input_type + "\"]").css("box-shadow", "");
}
function changeAlertMsgForRWD(){
    $("#alert-message").css("left", function(){
        return $(window).width() / 2 - $(this).outerWidth() / 2;
    })
}
$(document).ready(function(){
    changeAlertMsgForRWD();

    $(window).resize(function(){
        changeAlertMsgForRWD();
    })

    $("#profile_form").submit(function(event) {
        var email = $("#email").val();
        var phone = $("#phone").val();
        var id = $("#id").val();
        var pass = true;
        $('.form-control').each(function() {
            var text = $(this).val();
            var type = $(this).attr("type");
            var validate = chooseValidateMethod(type)
            if (!validate(text)){
                warningColor(type);
                if (pass == true){
                    alertWarning(type);
                }
                pass = false;
            }else{
                normalColor(type);
            }
        });
        if (!pass){
            event.preventDefault();
        }
    });

    $('.form-control').on('input', function(e) {
        var text = $(this).val();
        var type = $(this).attr("type");
        var validate = chooseValidateMethod(type)
        if (!validate(text)){
            warningColor(type);
        }else{
            normalColor(type);
        }

    });

    $('.form-control').each(function() {
        var text = $(this).val();
        var type = $(this).attr("type");
        var validate = chooseValidateMethod(type)
        if (!validate(text)){
            warningColor(type);
        }else{
            normalColor(type);
        }

    });
})



