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

/*
(function (jQuery) {
  jQuery.mark = {
    tabs: function (options) {
      var defaults = {
        selector: '.the-days'
      };
      if (typeof options == 'string') defaults.selector = options;
      var options = jQuery.extend(defaults, options);
      return jQuery(options.selector).each(function () {
        var tabobj = jQuery(this);
        var theprev = jQuery('.left');
        var thenext = jQuery('.right');
        var thepanes = tabobj.find('.navtab-content').hide();
        var d = new Date();
        var n = d.getDay();
        thepanes.eq(n).addClass('current-panel');
        thepanes.eq(n).find('h2').addClass("today");
        thepanes.eq(n).show();

        theprev.click(function(event){
          var curr = jQuery('.current-panel');
          if(curr.is(':first-child')) {
            curr.removeClass('current-panel').fadeOut(10);
            jQuery('.navtab-content:last').addClass('current-panel').slideDown(600);
          } else {
            curr.prev().addClass('current-panel').slideDown(600);
            curr.removeClass('current-panel').fadeOut(10);
          }
        });

        thenext.click(function(event){
          var curr = jQuery('.current-panel');
          if(curr.is(':last-child')) {
            jQuery('.navtab-content:first').addClass('current-panel').slideDown(600);
            curr.removeClass('current-panel').fadeOut(10);
          } else {
            curr.next().addClass('current-panel').slideDown(600);
            curr.removeClass('current-panel').fadeOut(10);
          }
        });


      })
    },
    doNotes: function (options) {
      var defaults = {
        selector: '.notes-module'
      };
      if (typeof options == 'string') defaults.selector = options;
      var options = jQuery.extend(defaults, options);
      return jQuery(options.selector).each(function () {
        var modobj = jQuery(this);
        var listobj = jQuery(this).find('ul');
        var storename = listobj.attr('id');
        var formobj = jQuery(this).find('form');
        var dataobj = formobj.find('input[type="text"]');
        if (localStorage.getItem(String(storename))) {
          listobj.html(localStorage.getItem(storename));
        }
        modobj.on("submit", "form", function(e){
          var textToAdd = '<li><i class="fa fa-trash"></i>' + dataobj.val() + '</li>';
          listobj.append(textToAdd);
          dataobj.val('').focus();
          localStorage.setItem(storename, listobj.html());
          e.preventDefault();
        });
        modobj.on("click", "li", function(){
          if (jQuery(this).hasClass('mark-me')) {
            jQuery(this).removeClass("mark-me");
            listobj.prepend(jQuery(this));
          } else {
          jQuery(this).addClass("mark-me");
          listobj.append(jQuery(this));
          }
          localStorage.setItem(storename, listobj.html());
        });
        modobj.on("click", "i.fa-trash", function(){
          jQuery(this).parent().fadeOut(500, function(){
            jQuery(this).remove();
            localStorage.setItem(storename, listobj.html());
          });
        });
      })
    }

  }
})(jQuery);

jQuery(function(){
  jQuery.mark.tabs();
  jQuery.mark.doNotes();
});ist */








