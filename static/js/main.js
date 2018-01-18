function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

nodefind_req = function(){
    $("#nodefind_result_msg").html("<div class='alert alert-info' role='alert'>" +  "searching, please wait......" + "</div>");
    $("#nodefind_result").html("");
    $("#nodefind_bt").attr("disabled", true);
    $.post("/nodefind", {
                        _xsrf:getCookie("_xsrf"),
                        ipaddr:$("#ip").val(),
                        username:$("#username").val(),
                        passwd:$("#passwd").val(),
                        devtype:$("#devtype").val()
                        },
                      function(data,textStatus){
      $("#nodefind_result_msg").html("");
      $("#nodefind_result").html(data);
      $("#nodefind_bt").attr("disabled", false);
    });
  };

wwnfind_req = function(){
    $("#wwnfind_result_msg").html("<div class='alert alert-info' role='alert'>" +  "searching, please wait......" + "</div>");
    $("#wwnfind_result").html("");
    $("#wwnfind_bt").attr("disabled", true);
    $.post("/wwnfind", {
                        _xsrf:getCookie("_xsrf"),
                        wwn:$("#wwn").val()
                        },
                      function(data,textStatus){
      $("#wwnfind_result_msg").html("");
      $("#wwnfind_result").html(data);
      $("#wwnfind_bt").attr("disabled", false);
    });
  };

zoning_req = function(){
  $("#zone_bt").attr("disabled", true);
  $("#zone_result_msg").html("<div class='alert alert-info' role='alert'>" +
                         "zoning, do Not create/delete zone in the same fabric until this is done. Please wait......" +
                         "</div>");
  if($("#zonename").val() && $("#wwns").val()){
    $.post("/zone", {
                      _xsrf:getCookie("_xsrf"),
                      zonename:$("#zonename").val(),
                      wwns:$("#wwns").val(),
                      fid_vsan:$("#fid_vsan").val()
                     },
                     function(data, textStatus){
      $("#zone_bt").attr("disabled", false);
      $("#zone_result_msg").html(data);
  });
  }else{
      $("#zone_bt").attr("disabled", false);
      $("#zone_result_msg").html("<div class='alert alert-danger' role='alert'>" +
                             "zone name and WWNs can't be empty!" +
                             "</div>");
  };
};

delete_zone_req = function(){
  $("#delete_bt").attr("disabled", true);
  $("#delete_result_msg").html("<div class='alert alert-info' role='alert'>" +
                         "deleting, DO NOT create/delete zone in the same fabric until this is done. Please wait......" +
                         "</div>");
  if($("#zonename").val()){
    $.post("/delete", {
                      _xsrf:getCookie("_xsrf"),
                      zonename:$("#zonename").val(),
                      fid_vsan:$("#fid_vsan").val()
                     },
                     function(data, textStatus){
      $("#delete_bt").attr("disabled", false);
      $("#delete_result_msg").html(data);
  });
  }else{
      $("#delete_bt").attr("disabled", false);
      $("#delete_result_msg").html("<div class='alert alert-danger' role='alert'>" +
                             "zone name can't be empty!" +
                             "</div>");
  };
};

searchzone_req = function(){
    $("#searchzone_result_msg").html("<div class='alert alert-info' role='alert'>" +  "searching, please wait......" + "</div>");
    $("#searchzone_result").html("");
    $("#searchzone_bt").attr("disabled", true);
    $.post("/search", {
                        _xsrf:getCookie("_xsrf"),
                        keyword:$("#keyword").val(),
                        fid_vsan:$("#fid_vsan").val()
                        },
                      function(data,textStatus){
      $("#searchzone_result_msg").html("");
      $("#searchzone_result").html(data);
      $("#searchzone_bt").attr("disabled", false);
    });
  };

del_zone_req = function(){
  $("#search_bt").toggle();
  $("#zoning_bt").toggle();
  $("#del_zoning_bt").toggle();
  $("#zone_result").html("<div class='alert alert-info' role='alert'>" +
                         "deleting zone, please wait......" +
                         "</div>");
  if($("#del_zone_name").val()){
    $.get("/delzone", {"zone_name":$("#del_zone_name").val(),
                       "dev":$("#del_slc_br_ci").val(),
                       "env":$("#del_slc_zone_env").val()},
                     function(data, textStatus){
      $("#search_bt").toggle();
      $("#zoning_bt").toggle();
      $("#del_zoning_bt").toggle();
      $("#zone_result").html("<div class='alert alert-success' role='alert'>" +
                             "zone delete success" +
                             "</div>");
  });
  }else{
      $("#search_bt").toggle();
      $("#zoning_bt").toggle();
      $("#del_zoning_bt").toggle();
      $("#zone_result").html("<div class='alert alert-danger' role='alert'>" +
                             "zone name can't be empty!" +
                             "</div>");
  };
};

$(document).ready(function(){

  $("#nodefind_bt").click(nodefind_req);
  $("#wwnfind_bt").click(wwnfind_req);
  $("#searchzone_bt").click(searchzone_req);
  $("#zone_bt").click(zoning_req);
  $("#delete_bt").click(delete_zone_req);


});
