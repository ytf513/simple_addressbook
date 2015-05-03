$(document).ready(function(){
    $('input').focus(function(){
        $(this).css('outline-color','#0000ff');
    });
   /* $('.ipt-text').keyup(function(){
        $.get("/ajaxGet?search="+$(this).val(),function(data,status){
           //alert(data["data"]); 
           $(this).autocomplete({
                 source:data
           });
        }); 
    })*/

 $(".ipt-text").autocomplete({
    source: function( request, response ) {
        $.ajax({
          url: "/ajaxGet",
          dataType: "json",// jsonp not action
          data: {
            search: request.term
          },
          success: function( data ) {
            response(data["data"]);
            //alert(data["data"]);
          }
        });
      },
    minLength: 1,
    select: function(event, ui) { 
        //返回数据类似"尹天峰 20822"，所以如下是截取空格后面字符，即“20822”        
    	$(this).val(ui.item.value.split(" ")[1]);
    	$("#searchform").submit(); //提交当前页面
    }
  });    

})
