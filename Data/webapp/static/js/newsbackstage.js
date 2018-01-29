window.onload=function(){
	initbody()
	bar()
	textedite()
	

}

function loadLocal(){
    new PCAS("province6","city6","area6","湖南省","长沙市","芙蓉区");
}

function initbody(){
	var yes=$("#yes")
	var cancel=$("#cancel")
	yes.getEl(0).onmousedown=function(){
		yes.css("color:#FFF")

	}
	yes.getEl(0).onmouseup=function(){
		yes.css("color:red")
	}

	cancel.getEl(0).onmousedown=function(){
		cancel.css("color:#FFF")
	}
	cancel.getEl(0).onmouseup=function(){
		cancel.css("color:red")
	}


	var headp = document.getElementById("headp")
    headp.style.width = headp.offsetHeight + "px"


}


/*
* 标题栏功能
* */
function bar() {
    var ob = $("#list").findchild("li")
    var head = $("#headp").getEl(0)
    head.onclick = function () {
        window.location.href = "userInfo"
    }
    for (var i = 0; i < 7; i++) {
        (function (i) {
            ob.getEl(i).onclick = function () {
                var text = this.innerText.replace(/\s+/g, "")
                var local = "*"
                var flag = 0
                var tag = 1
                var from = "indexbar"
                if (text == "县/区") {
                    flag = 1
                }
                else if (text == "市级") {
                    flag = 2
                }
                else if (text == "省级") {
                    flag = 3
                }
                else if (i <= 4 & i > 0 & text != "自分组") {
                    local = text
                    flag = i - 1
                    tag = 2
                }

                if (i == 0)
                    window.location.href = "index"
                if (i <= 4 & i > 0) {
                    $().ajax({
                        "type": "post",
                        "url": "newslist",
                        "data": {"local": local, "flag": flag, "tag": tag, "from": from},
                        "fn": function (value) {
                            window.location.href = value.responseText
                        }
                    })
                }
                if (text == "登录") {
                    window.location.href = "loading"
                }
                if (text == "退出") {
                    window.location.href = "quite"
                }
                if (text == "注册") {
                    window.location.href = "regist"
                }


            }
        })(i)
    }
}


/*
 文本编辑
*/
files=""
function textedite()
{ var si=5
  var ob=$("#font ul li")
  ob.getEl(0).onclick=function(e)
  {
  	document.execCommand("Width",0,"7px")
  	

  }
  ob.getEl(1).onclick=function(e)
  {
  	document.execCommand("JustifyCenter")

  }
   ob.getEl(2).onclick=function(e)
  {
  	document.execCommand("JustifyRight")
  }
   ob.getEl(3).onclick=function(e)
  {
  	document.execCommand("Bold")
  }
   ob.getEl(4).onclick=function(e)
  {
  	colorpicker(e,"BackColor")
  }
   ob.getEl(5).onclick=function(e)
  { if(si<7)
  	si+=1
  	document.execCommand("FontSize","false",si)

  }
   ob.getEl(6).onclick=function(e)
  { if(si>1)
  	 si-=1
  	document.execCommand("FontSize","false",si)
  }
    
  ob.getEl(7).onclick=function(e)
  {
  	colorpicker(e,"ForeColor")
  }
  ob.getEl(8).onclick=function(e)
  {   
      ob.getEl(8,"$").css("display:none")
      ob.getEl(9,"$").css("display:block")
      var t=$("#file").getEl(0)
  	    t.click()

  	   
  }
  ob.getEl(9).onclick=function()
  {
  	var t=$("#file").getEl(0).files[0]
  	$().ajax({
  		"type":"post",
  		"url":"file",
  		"data":{"file":t},
  		"fn":function(value)
  		{  
  			 $("#content").getEl(0).focus()
  			document.execCommand('InsertImage',false,value.responseText);
  			contentimgsize()
  		}
  	})
  	  ob.getEl(9,"$").css("display:none")
  	  ob.getEl(8,"$").css("display:block")
  	  
    
  	
  }
  ob.getEl(10).onclick=function(e)
  {
  	document.execCommand("Undo")
  }
}


/*
修改图片大小
*/

function contentimgsize()
{
	var abc=document.getElementById("content").getElementsByTagName("img")
	var all=abc.length
	for(var i=0;i<all;i++)
	{
      (
        function(i)
        {  
        	abc[i].onclick=function()
        	{ 
        		var imgsize=$(".imgsize")
        		var temp=this
        		imgsize.css("display:block")
        		var chil=imgsize.findchild("input")
        		chil.getEl(2).onclick=function()
        		{
        			temp.style.width=chil.getEl(0).value+"px"
        			temp.style.height=chil.getEl(1).value+"px"
        			$(".imgsize").css("display:none")

        		}
        	}
        	
        	
        }
      	)(i)
	}
	
}