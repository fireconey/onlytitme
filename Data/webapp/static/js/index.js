window.onload = function () {    initbody();    changelabel()    showdetail()    tolist()    bar()    window.setInterval(function (args) {        filldata()    },2000)}window.onresize = function () {    initbody();}function initbody() {    var h = window.innerHeight;    var ob = document.getElementById("container");    var w = ob.offsetWidth;    ob.style.height = w / 0.3319016 + "px";    var headp = document.getElementById("headp")    headp.style.width = headp.offsetHeight + "px"    var img = $(".photo").getEl("all")    var imgh = img[0].offsetHeight    for (var i in img) {        img[i].style.width = imgh + "px"    }}//点击对应组的对应分类进入对应分类的列表/**1、使用一个参数来标记展示那段数据flag*2、flag:表示第几组的数据* 3、local表示地区的数据* 4、n，m表示要查询的分段，便于滚动*** */function filldata() {    var label = $(".tag").findchild("a")    var title = $(".text")    var img = $(".photo")    var name = $(".name")    var temp = 0    var state = 2    if (tool2(label.getEl(0)) == "自分组") {        var local = tool2(label.getEl(0))        fillpart(local, 0, 1)    }    if (tool2(label.getEl(1)) == "县/区") {        var local = tool2(label.getEl(1))        fillpart(local, 1, 1)    }    if (tool2(label.getEl(2)) == "市级") {        var local = tool2(label.getEl(2))        fillpart(local, 2, 1)    }    if (tool2(label.getEl(3)) == "省级") {        var local = tool2(label.getEl(3))        fillpart(local, 3, 1)    }    function fillpart(local, flag, state) {        $().ajax({            "type": "post",            "url": "index",            "data": {"local": local, "flag": flag, "n": 0, "m": 15, "tag": "fill", "state": state},            "fn": function (value) {                temp = tool(value.responseText)                temp = JSON.parse(temp)                // temp=JSON.parse(value)                for (var j = 0; j < 15; j++) {                    title.getEl(flag * 15 + j).innerText = temp["title"][j]                    name.getEl(flag * 15 + j).innerText = temp["usr"][j]                    img.getEl(flag * 15 + j).setAttribute("src", temp["img"][j])                }            }        });    }}/**查询不同地区的数据* */function changelabel() {    var title = $(".tag").findchild("a")    var changeinput = $(".changeinput")    var changeyes = $(".changeyes")    title.getEl(0).innerText = "自分组------>>>"    title.getEl(1).innerText = "县/区------>>>"    title.getEl(2).innerText = "市级------>>>"    title.getEl(3).innerText = "省级------>>>"    for (var i = 0; i < 4; i++) {        (            function (value) {                changeyes.getEl(value).onclick = function () {                    $().ajax({                        "type": "post",                        "url": "index",                        "data": {"local": changeinput.getEl(value).value, "flag": value, "tag": "qry"},                        "fn": function (some) {                            var result = tool(some.responseText)                            result = JSON.parse(result)                            if (result["result"]) {                                title.getEl(value).innerText = changeinput.getEl(value).value + "------>>>"                                changeinput.getEl(value).value = ""                                filldata(value, changeinput.getEl(value).value, 0, 15)                            }                            else {                                alert("没有此地区的数据")                            }                        }                    })                }            }        )(i)    }}/** 点击不同的标签进入详情页面* */function showdetail() {    var ob = $(".li")    var title = $(".text")    var name = $(".name")    for (var i = 0; i < 4; i++) {        for (var j = 0; j < 15; j++) {            (function (value) {                    ob.getEl(value).onclick = function () {                        $().ajax(                            {                                "type": "post",                                "url": "timenewsdetail",                                "data": {"title": title.getEl(value).innerText, "name": name.getEl(value).innerText},                                "fn": function (value) {                                    window.location.href = value.responseText                                }                            }                        )                    }                }            )(i * 15 + j)        }    }}/** 点击分组的标签进入列表栏* */function tolist() {    var title = $(".tag").findchild("a")    for (var i = 0; i < 4; i++) {        (function (value) {            var local = title.getEl(value).innerText.replace(/------>>>/g, "")            var tag = 2            title.getEl(value).onclick = function () {                if (local == "自分组") {                    local = "*"                    tag = 1                }                if (local == "县/区") {                    local = "*"                    tag = 1                }                if (local == "市级") {                    local = "*"                    tag = 1                }                if (local == "省级") {                    local = "*"                    tag = 1                }                $().ajax({                    "type": "post",                    "url": "newslist",                    "data": {"flag": value, "local": local, "tag": tag, "from": "indexlabel"},                    "fn": function (some) {                        window.location.href = "newslist"                    }                })            }        })(i)    }}/** 标题栏功能* */function bar() {    var ob = $("#list").findchild("li")    var head = $("#headp").getEl(0)    head.onclick = function () {        window.location.href = "userInfo"    }    for (var i = 0; i < 7; i++) {        (function (i) {            ob.getEl(i).onclick = function () {                var text = this.innerText.replace(/\s+/g, "")                var local = "*"                var flag = 0                var tag = 1                var from = "indexbar"                if (text == "县/区") {                    flag = 1                }                else if (text == "市级") {                    flag = 2                }                else if (text == "省级") {                    flag = 3                }                else if (i <= 4 & i > 0 & text != "自分组") {                    local = text                    flag = i - 1                    tag = 2                }                if (i == 0)                    window.location.href = "index"                if (i <= 4 & i > 0) {                    $().ajax({                        "type": "post",                        "url": "newslist",                        "data": {"local": local, "flag": flag, "tag": tag, "from": from},                        "fn": function (value) {                            window.location.href = value.responseText                        }                    })                }                if (text == "登录") {                    window.location.href = "loading"                }                if (text == "退出") {                    window.location.href = "quite"                }                if (text == "注册") {                    window.location.href = "regist"                }            }        })(i)    }}function tool(value) {    var result = value.replace(/\s+/g, "")    result = result.replace(/\'/g, '"')    return result}function tool2(value) {    var result = value.innerText.replace(/\------>>>/g, "").replace(/\s+/g, "")    return result}