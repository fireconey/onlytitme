function  head(){
	img();
	bar()

}
function img(){
	var ob=document.getElementsByName("mark")[0];
	var img=document.getElementById("headp");
	    img.style.width=img.offsetHeight+"px"
	img.onclick=function(){
		ob.value="img";
		ob.click();
	}
}

function bar(){

	var ob=$("#list").findchild("li")
	var head=$("#headp").getEl(0)
	head.onclick=function(){
		window.location.href="userInfo"
	}
	for(var i=0;i<7;i++)
	{
		(function(i){
			ob.getEl(i).onclick=function(){
				var text=this.innerText.replace(/\s+/g,"")
				var local = "*"
                var flag = 0
				var	tag=1
				var	from="indexbar"
                if(text=="县/区")
				{
					flag=1
				}
				else if(text=="市级")
				{
					flag=2
				}
				else if(text=="省级")
				{
					flag=3
				}
				else if(i<=4 & i>0&text!="自分组")
				{
					local =text
                	flag =i-1
					tag=2
				}

				if(i==0)
					window.location.href="index"
                if(i<=4 & i>0)
                {
					$().ajax({
						"type":"post",
						"url":"newslist",
						"data":{"local":local,"flag":flag,"tag":tag,"from":from},
						"fn":function(value){
							window.location.href=value.responseText
						}
					})
				}
				if(text=="登录")
				{
					window.location.href="loading"
				}
				if(text=="退出")
				{
					window.location.href="quite"
				}
				if(text=="注册")
				{
					window.location.href="regist"
				}


			}
		})(i)
	}

}
