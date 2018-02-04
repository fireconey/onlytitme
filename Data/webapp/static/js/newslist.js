window.onload=function(){
	head()
	initbody()
	filldata()
	button()
	showdetail()
	changlabel()
}   

window.onresize=function() {
    initbody()
}

function initbody(){
	var container=document.getElementById("container")
	    container.style.height=container.offsetWidth/0.42183623+"px"
	var hg=document.getElementById("headp")
	    hg.style.height=hg.offsetWidth+"px"
	var img=document.getElementById("headp");
	    img.style.width=img.offsetHeight+"px"
	var headimg=$(".headimg")
	for(var i=0;i<60;i++)
	{
		headimg.getEl(i).style.width=headimg.getEl(i).offsetHeight+"px"
	}

}
count=1


function filldata(){
	var img=$(".headimg")
	var nam=$(".name")
	var content=$(".data")
	var all=$("#all")
	$().ajax({
		"type":"post",
		"url":"newslist",
		"data":{"count":count,"from":"newslist"},
		"fn":function(value)
		{
			var v=value.responseText.replace(/\'/g,'"')
			var json=JSON.parse(v)
			all.innerText=json['all']

			for(var i=0;i<60;i++)
			{
				img.getEl(i).setAttribute("src",json["img"][i])
				nam.getEl(i).innerText=json["usr"][i]
				content.getEl(i).innerText=json["title"][i]
			}

		}
	})



}

function button(){
	var pre=$("#pre").getEl(0)
	var next=$("#next").getEl(0)
	var ipt=$("#ipt").getEl(0)
	var all=$("#all").getEl(0)
	var yes=$("#yes").getEl(0)

	pre.onclick=function()
	{
		if(ipt.value>=2)
		{   count-=1
            ipt.value=count

			filldata()
		}
    }
    next.onclick=function(){

		var num=all.innerText.trim()



		if (num>=count+1 )
        {
			count+=1
			ipt.value=count
			filldata()

        }
	}
	yes.onclick=function (){
		if(ipt.value>=1&ipt.value<=all.innerText.replace(/\s+/g,""))
		{
			count=ipt.value
			filldata()
		}
		else{
			alert("你输入的页数超过规定值(目前为:"+ipt.value+")")
		}
	}

}

function showdetail(){
	var clc=$(".clickbolck")
	var nameob=$(".name")
	var titleob=$(".data")
	for(var i=0;i<60;i++)
	{
		(function (v) {
			clc.getEl(v).onclick=function(){
				var usr=nameob.getEl(v).innerText.trim()
				var title=titleob.getEl(v).innerText.trim()
				if(title=="无数据")
				{  alert("无数据")
					return  "temp"}
				document.cookie="_name="+encodeURIComponent(usr)+";"
				document.cookie="_title="+encodeURIComponent(title)+";"
				window.location.href="timenewsdetail"

			}
        })(i)
	}
}

function changlabel() {
    var title = $(".tag").findchild("a").getEl(0)
    var changinput = $(".changeinput").getEl(0)
    var changeyes = $(".changeyes").getEl(0)
	var flag=$("#flag").getEl(0)
   changeyes.onclick=function()
   {
   	document.cookie="_local="+encodeURIComponent(changinput.value)
    document.cookie="_tag="+encodeURIComponent("2")
	   document.cookie="_search=yes" //用于标记点击了查询的按钮
	window.location.href="newslist"
   }

}