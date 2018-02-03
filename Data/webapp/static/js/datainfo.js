window.onload = function () {
    initbody()
    img()
    bar()
    filldata(1)
    showparper()
    delet()
    manager()

}

//由于标记是第几页
var count = 1

window.onresize = function () {
    initbody()

}

function initbody() {
    var ob = document.getElementById("inner")
    var w = ob.offsetWidth
    ob.style.height = w / 0.795 + "px"
    var headp = document.getElementById("headp")
    headp.style.width = headp.offsetHeight + "px"


}


function img() {
    var ob = document.getElementsByName("mark")[0];
    var img = document.getElementById("headp");
    img.onclick = function () {
        ob.value = "img";
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
all=1
function filldata(count) {
    var span = $("#items ul li span")
    $().ajax({
        "type": "post",
        "url": "info",
        "data": {"count": count, "flag": "fill"},
        "fn": function (value) {
            var v = value.responseText.replace(/\'/g, '"')
            var json = JSON.parse(v)
            len = json["title"].length
            all=json["all"]
            //解决数据删除后，数据库修改了，原来的
            //位置数据没有刷新的问题。
            for (var i = 0; i < 10; i++)
                span.getEl(i).innerText = ""

            for (var i = 0; i < len; i++) {   //由于数据库是栈的形式所以要倒序填充数据
                //-1是由于长度和下标相差1
                var data = json["title"][len - 1 - i]
                if (typeof(data) != "undefined") {
                    span.getEl(i).innerText = (count - 1) * 10 + (i + 1) + "*》" + data
                }
                else {
                    span.getEl(i).innerText = ""

                }

            }
        }
    })
}


/*
* 点击后显示具体内容
* */
function showparper() {
    var ob = $("#items ul li span")
    var content = $("#text").getEl(0)
    for (var i = 0; i < 10; i++) {
        (
            function (i) {
                ob.getEl(i).onclick = function () {
                    var title = this.innerText.split("*》")[1].replace(/\s+/g, "");
                    if (title != "") {
                        $().ajax({
                            "type": "post",
                            "url": "info",
                            "data": {"title": title, "flag": "content"},
                            "fn": function (value) {
                                content.innerHTML = value.responseText

                            }

                        })
                    }
                }
            }
        )(i)
    }
}

/*
* 点击删除就删除
* */
function delet() {
    var ob = $("#items ul li .delet")
    var content = $("#text")
    for (var i = 0; i < 10; i++) {
        (
            function (i) {
                ob.getEl(i).onclick = function () {
                    var title = this.previousSibling.previousSibling.previousSibling.previousSibling.innerText.replace(/\s+/g, "").split("*》")[1]
                    $().ajax({
                        "type": "post",
                        "url": "info",
                        "data": {"title": title, "flag": "delet"},
                        "fn": function (value) {
                            filldata(count)
                            content.getEl(0).innerText = ""
                        }
                    })

                }
            }
        )(i)
    }
}

/*
* 点击管理进入管理界面
* */
function manager() {
    var ob = $("li .change")
    var titl = $("li span")
    for (var i = 0; i < 10; i++) {
        (function (i) {
                ob.getEl(i).onclick = function () {
                    title = titl.getEl(i).innerText.replace(/\s+/g,"").split("*》")[1]
                    if(typeof(title)!="undefined")
                    {
                        document.cookie="_title="+encodeURIComponent(title)+";"
                        document.cookie="_tag=manager" //由于区分进入后台的是哪个前端
                        window.location.href="newsbackstage"
                    }

                }
            }
        )(i)
    }

}