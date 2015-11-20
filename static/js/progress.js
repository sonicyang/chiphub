$(document).ready(function() {
  function modifValues(){
    var val = $('.downloading-progress-bar').attr('data-value');
    if(val>=100){val=5;}
    var newVal = val*1+0.5;
    var txt = Math.floor(newVal)+'%';

    $('.downloading-progress-bar').attr('data-value',newVal);
    $('.percentage').html(txt);
    $('.downloading-progress-bar').css("width", txt);
  }

  setInterval(function(){ modifValues(); },50);

}
