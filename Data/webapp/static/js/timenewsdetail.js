window.onload = function () {
    initbody()
    img()
    bar()
    filleval()

}

window.onresize = function () {
    initbody()
}


function initbody() {
    var ob = document.getElementById("inner")
    var w = ob.offsetWidth
    // ob.style.height = w / 0.8752 + "px"
    // alert(ob.offsetHeight)
    var headp = document.getElementById("headp")
    var img2=document.getElementById("img2")
    headp.style.width = headp.offsetHeight + "px"
    // img2.style.width = img2.offsetHeight + "px"
}

function img() {
    var ob = document.getElementsByName("mark")[0];
    var img = document.getElementById("headp");
    img.onclick = function () {
        ob.value = "img";
        ob.click();
    }

}


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
加载评论
*/

function filleval()
{  
  var name=$("#usr").getEl(0).innerText.replace(/\s+/g,"")
  var title=$("#title").getEl(0).innerText.replace(/\s+/g,"")


 $().ajax({
    "type":"post",
    "url":"eval",
    "data":{"title":title,"usr":name,"flag":"fill"},
    "fn":function(value)
    { 
        var li=""
        var ob=$("#othereva").getEl(0)
        var json=JSON.parse(value.responseText)
        for(var i=0;i<json["name"].length;i++)
        {
            var ele="<ul class='ul'>"+
                    "<li class='li1 li'>"+
                        "<img src='"+json["img"][i]+"' alt='浮动''>"+
                        "<div class='othername'>"+json["name"][i]+"</div>"+
                    "</li>"+
                    " <li class='li2 li'>"+
                    json["content"][i]+
                    "</li>"+
                "</ul>"
                li=li+ele
                
        }
        if(json["name"].length!=0)
        {
             ob.innerHTML=li
            var hp=$(".li1 img")
            all=hp.getEl("all").length
            for(var j=0;j<all;j++)
            {
                hp.getEl(j).style.width=hp.getEl(j).offsetHeight+"px"
            }
        }
       
        


            
    }
    })
    
    
}
