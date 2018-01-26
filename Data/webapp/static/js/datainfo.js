window.onload=function(){
	initbody()
	img()
	bar()
    filldata(1)
    showparper()

}


window.onresize=function(){
	initbody()

}

function initbody(){
	var ob=document.getElementById("inner")
	var w=ob.offsetWidth
	    ob.style.height=w/0.795+"px"
	     var headp=document.getElementById("headp")
	    headp.style.width=headp.offsetHeight+"px"
	    
	   
}


function img(){
	var ob=document.getElementsByName("mark")[0];
	var img=document.getElementById("headp");
	img.onclick=function(){
		ob.value="img";
		ob.click();
	}

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
* 数据填充
* */
function filldata(count){
    var li=$("#items").findchild("ul").findchild("li")
    $().ajax({
        "type":"post",
        "url":"info",
        "data":{"count":count,"flag":"fill"},
        "fn":function(value){
            var v=value.responseText.replace(/\'/g,'"')
            var json=JSON.parse(v)
            for(var i=0;i<10;i++)
            {
                var data=json["title"][i]
                if(typeof(data)!="undefined")
                {
                    li.getEl(i).innerText=(count-1)*10+(i+1)+"*》"+data
                }

            }
        }
    })
}


/*
* 点击后显示具体内容
* */
function  showparper()
{
    var ob = $("#items").findchild("ul").findchild("li");
    var content=$("#text").getEl(0)
    for(var i=0;i<10;i++)
    {
        (
            function(i)
            {
                ob.getEl(i).onclick=function()
                {
                    var title= this.innerText.split("*》")[1].replace(/\s+/g, "");

                  $().ajax({
                      "type":"post",
                      "url":"info",
                      "data":{"title":title,"flag":"content"},
                      "fn":function(value){
                          content.innerHTML=value.responseText

                      }

                  })
                }
            }
        )(i)
    }
}
