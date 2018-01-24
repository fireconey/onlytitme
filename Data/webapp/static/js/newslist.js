window.onload=function(){
	head()
	initbody()
	filldata()
	button()
	showdetail()
}   

window.onresize=function() {
    initbody()
}

function initbody(){
	var container=document.getElementById("container")
	    container.style.height=container.offsetWidth/0.42183623+"px"
	var hg=document.getElementById("headp")
	    hg.style.height=hg.offsetWidth+"px"


}
count=1


function filldata(){
	var img=$(".headimg")
	var nam=$(".name")
	var content=$(".data")
	$().ajax({
		"type":"post",
		"url":"newsList",
		"data":{"count":count},
		"fn":function(value)
		{
			var v=value.responseText.replace(/\'/g,'"')
			var json=JSON.parse(v)
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
		if (all.innerText.replace(/\s+/g, "") >=count+1 )
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
	var left=$(".clickbolck")
	var name=$(".name")
	var title=$(".data")
	for(var i=0;i<60;i++)
	{
		(function (v0,v1,v2,v3) {
			v0.getEl(v3).onclick=function(){
				$().ajax({
				"type":"post",
				"url":"timenewsdetail",
				"data":{"name":name.getEl(v3).innerText,
					"title":title.getEl(v3).innerText},
					"fn":function(value){
					 window.location.href=value.responseText
					},
				"fn":function(value) {
					window.location.href=value.responseText
                }
			})
			}
        })(left,name,title,i)
	}
}


