window.onload=function(){
	head()
    initbody()
	filldata()
	button()
}
window.onresize=function(){
	initbody()
}

function initbody(){
	var ob=document.getElementById("container")
	    ob.style.height=ob.offsetWidth/0.18012+"px"

	var hg=document.getElementById("headp")
	    hg.style.width=hg.offsetHeight+"px"
}


count=1
function filldata(){
	var gsphotoimg=$(".gsphoto")
	var hphoto=$(".hphoto")
	var title=$(".title")
	var price=$(".price")

	$().ajax({
		"type":"post",
		"url":"goodsList",
		"data":{"count":count},
		"fn":function(value)
		{
			var v=value.responseText.replace(/\'/g,'"')
			var json=JSON.parse(v)
			for(var i=0;i<80;i++)
			{
				hphoto.getEl(i).setAttribute("src",json["img"][i])
				gsphotoimg.getEl(i).setAttribute("src",json["img"][i])
                title.getEl(i).innerText=json["title"][i]
				price.getEl(i).innerText=json["price"][i]
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
			alert("你输入的页数超过规定值(目前为："+ipt.value+")")
		}
	}

}