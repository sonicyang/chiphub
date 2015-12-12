app.controller('chatroom-ctrl', function($scope, $http, $rootScope) {
    $scope.infoing = false;
    $scope.families = [];

    $http.get("/chatroom/top100/")
        .then(function(response){
            $scope.families = response.data;
        });

    $scope.show_info = function(family, chip){
        $scope.infoing = true;
        $scope.info = chip;
        $scope.info_family = family;
    };
});

//function showPNs(pn_info_list){
    //var pn_info_dict = {};
    //for (var i = 0; i < pn_info_list.length; i ++){
        //var family = pn_info_list[i]['ctype']['mname'] + pn_info_list[i]['ctype']['sname'];
        //var name = pn_info_list[i]['common_name'];
        //if (pn_info_dict[name] !== undefined){
            //appendChipCard(pn_info_list[i]);
            //pn_info_dict[name] = 1;
        //}else{
            //appendFamily(pn_info_list[i]);
            //pn_info_dict[name] += 1;
        //}
    //}
//}
//function appendFamily(pn){
    //var family_name = pn['ctype']['mname'] + pn['ctype']['sname'];
    //$("#chip-card-list").append(family_html);
    //$("#chip-card-list .family").last().attr("name", family_name.hashCode())
    //$("#chip-card-list .family").last().find(".family-mname").text(pn['ctype']['mname'])
    //$("#chip-card-list .family").last().find(".family-sname").text(pn['ctype']['sname'])
    //appendChipCard(pn);
//}
//function appendChipCard(pn){
    //var family_name = pn['ctype']['mname'] +  pn['ctype']['sname'];
    //var family_pattern = ".family" + "[name=" + family_name.hashCode() + "]"
    //$(family_pattern).append(chip_card_html);
    //$(family_pattern+ " a label ").last().text(pn['common_name']);
    //console.log(pn['common_name'])
//}
            //},function(response){
                //alert("Error !");
            //});
//});

//var family_html = "\
//<div  class=\"family\">\
    //<h3 class=\"family-mname\"></h3>\
    //<h5 class=\"family-sname\"></h5>\
//</div>\
//<hr />\
//"

//var chip_card_html = "\
    //<a class=\"chip-card bg-info\" href=\"#\">\
        //<label>\
         //QWERTYQ\
        //</label>\
    //</a>\
//"

//String.prototype.hashCode = function() {
    //var hash = 0, i, chr, len;
    //if (this.length === 0) return hash;
    //for (i = 0, len = this.length; i < len; i++) {
        //chr   = this.charCodeAt(i);
        //hash  = ((hash << 5) - hash) + chr;
        //hash |= 0; // Convert to 32bit integer
    //}
    //return hash;
//};

//$("#close-chip-info").click(function(){
    //$("#chip-info").fadeOut(500);
//})

//$(document).on('keyup',function(evt) {
    //if (evt.keyCode == 27) {
        //$("#chip-info").fadeOut(500);
        //disableEditPaidInfoMode();
    //}
//});

//$("#search").click(function(e){
    //search(e);
//})

//function search(e){
    //var pn = $("#part-number").text();
//}

//$.get("/chatroom/top100/")
//.success(function(data){
    //var pk_list = JSON.parse(data);
    //getPNs(pk_list);
//})
//.error(function(d){
    //alert("Error !");
//})

//function getPNs(pk_list){
    //var pn_info_list = [];
    //var counter = 0;
    //for (var i = 0; i < pk_list.length; i ++){
        //(function(x){
            //$.get("/chatroom/get_component_info/",
                  //{"pk": pk_list[x]})
                  //.success(function(data){
                      //pn_info_list[x] = JSON.parse(data);
                      //counter += 1
                      //if (counter == pk_list.length){
                          //showPNs(pn_info_list)
                      //}
                  //})
        //})(i);
    //}
//}

//function showPNs(pn_info_list){
    //var pn_info_dict = {};
    //for (var i = 0; i < pn_info_list.length; i ++){
        //var family = pn_info_list[i]['ctype']['mname'] + pn_info_list[i]['ctype']['sname'];
        //var name = pn_info_list[i]['common_name'];
        //if (pn_info_dict[name] !== undefined){
            //appendChipCard(pn_info_list[i]);
            //pn_info_dict[name] = 1;
        //}else{
            //appendFamily(pn_info_list[i]);
            //pn_info_dict[name] += 1;
        //}
    //}
//}
//function appendFamily(pn){
    //var family_name = pn['ctype']['mname'] + pn['ctype']['sname'];
    //$("#chip-card-list").append(family_html);
    //$("#chip-card-list .family").last().attr("name", family_name.hashCode())
    //$("#chip-card-list .family").last().find(".family-mname").text(pn['ctype']['mname'])
    //$("#chip-card-list .family").last().find(".family-sname").text(pn['ctype']['sname'])
    //appendChipCard(pn);
//}
//function appendChipCard(pn){
    //var family_name = pn['ctype']['mname'] +  pn['ctype']['sname'];
    //var family_pattern = ".family" + "[name=" + family_name.hashCode() + "]"
    //$(family_pattern).append(chip_card_html);
    //$(family_pattern+ " a label ").last().text(pn['common_name']);
    //console.log(pn['common_name'])
//}

