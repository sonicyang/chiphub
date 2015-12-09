var family_html = "\
<div  class=\"family\">\
    <h3 class=\"family-mname\"></h3>\
    <h5 class=\"family-sname\"></h5>\
</div>\
<hr />\
"

var chip_card_html = "\
    <a class=\"chip-card bg-info\" href=\"#\">\
        <label>\
         QWERTYQ\
        </label>\
    </a>\
"

String.prototype.hashCode = function() {
    var hash = 0, i, chr, len;
    if (this.length === 0) return hash;
    for (i = 0, len = this.length; i < len; i++) {
        chr   = this.charCodeAt(i);
        hash  = ((hash << 5) - hash) + chr;
        hash |= 0; // Convert to 32bit integer
    }
    return hash;
};

$(document).ready(function(){
    $("#close-chip-info").click(function(){
        $("#chip-info").fadeOut(500);
    })

})

$(document).on('keyup',function(evt) {
    if (evt.keyCode == 27) {
        $("#chip-info").fadeOut(500);
        disableEditPaidInfoMode();
    }
});


$("#search").click(function(e){
    search(e);
})

function search(e){
    var pn = $("#part-number").text();
}

$.get("/chatroom/top100/")
.success(function(data){
    var pk_list = JSON.parse(data);
    getPNs(pk_list);
})
.error(function(d){
    alert("Error !");
})

var pn_info_list = [];

function getPNs(pk_list){
    var counter = 0;
    for (var i = 0; i < pk_list.length; i ++){
        (function(x){
            $.get("/chatroom/get_component_info/",
                  {"pk": pk_list[x]})
                  .success(function(data){
                      pn_info_list[x] = JSON.parse(data);
                      counter += 1
                      if (counter == pk_list.length){
                          showPNs(pn_info_list)
                      }
                  })
        })(i);
    }
}

function showPNs(pn_info_list){
    var pn_info_dict = {};
    for (var i = 0; i < pn_info_list.length; i ++){
        var family = pn_info_list[i]['ctype']['mname'] + pn_info_list[i]['ctype']['sname'];
        var name = pn_info_list[i]['common_name'];
        if (pn_info_dict[name] !== undefined){
            appendChipCard(i);
            pn_info_dict[name] = 1;
        }else{
            appendFamily(i);
            pn_info_dict[name] += 1;
        }
    }
}
function appendFamily(s){
    pn = pn_info_list[s]
    var family_name = pn['ctype']['mname'] + pn['ctype']['sname'];
    $("#chip-card-list").append(family_html);
    $("#chip-card-list .family").last().attr("name", family_name.hashCode())
    $("#chip-card-list .family").last().find(".family-mname").text(pn['ctype']['mname'])
    $("#chip-card-list .family").last().find(".family-sname").text(pn['ctype']['sname'])
    appendChipCard(s);
}
function appendChipCard(s){
    pn = pn_info_list[s]
    var family_name = pn['ctype']['mname'] +  pn['ctype']['sname'];
    var family_pattern = ".family" + "[name=" + family_name.hashCode() + "]"
    $(family_pattern).append(chip_card_html);
    $(family_pattern+ " a label ").last().text(pn['common_name']);
    $(family_pattern+ " a ").last().attr("index", s);
    $(family_pattern+ " a ").click(function(){
        $(".comment").remove();
        var ind = $(this).attr("index");
        fillInfo(pn_info_list[ind])

        $.get("/chatroom/get_component_comments?pk=" + pn_info_list[ind]['id'], function(e){
            comments = JSON.parse(e);
            for(comment of comments){
                addComment(comment);
            }
        })

        $("#chip-info").fadeIn(500);
    })

}

function fillInfo(part){
    ci = $("#chip-info");
    $(".info-container h1").text(part["common_name"]);
    $("#info-type").text(part["ctype"]["mname"]);
    $("#info-family").text(part["ctype"]["sname"]);
    $("#info-rank").text(part["rank"]);
    $("#info-unit-price").text(part["digikey"]["unit_price"]);
}

var comment_html = "\
    <div class=\"row comment\">\
        <div class=\"grid group info-comment info-grid col-md-10\">\
            <div class=\"info-module\">\
                <h3 class=\"comment-title\">BOB - 2055/12/31</h3>\
                <div class=\"comment-context\">\
                    This chip Sucks\
                </div>\
            </div>\
        </div>\
        <div class=\"grid group info-parties info-grid col-md-1\">\
            <div class=\"info-module rank\">\
                <h4>RANK</h4>\
                <label class=\"comment-rank\">RANK</label>\
            </div>\
        </div>\
        <div class=\"grid group info-parties info-grid col-md-1\">\
            <div class=\"info-module-half rank\">\
                <i class=\"material-icons\">thumb_up</i>\
            </div>\
            <div class=\"info-module-half rank\">\
                <i class=\"material-icons\">thumb_down</i>\
            </div>\
        </div>\
    </div>\
"

function addComment(comment){
    comment_tag = $("#comment-container").append(comment_html)
    comment_tag.find(".comment-title").last().text(comment["commenter"] + " - " + comment["date"])
    comment_tag.find(".comment-context").last().text(comment["text"])
    comment_tag.find(".comment-rank").last().text(comment["rank"])
}
