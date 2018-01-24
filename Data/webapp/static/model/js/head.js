function  head(){
	img();
	topbar();

}
function img(){
	var ob=document.getElementsByName("mark")[0];
	var img=document.getElementById("headp");
	    // img.style.width=img.offsetHeight+"px"
	img.onclick=function(){
		ob.value="img";
		ob.click();
	}
}


function topbar() {
	var ul=document.getElementById("list");
	var mark=document.getElementsByName("mark")[0]
    var ch=ul.children
	var index=["index","newsList","goodsDetail","loading","regist"]
	ob0=ch[0]
	ob1=ch[1]
	ob2=ch[2]
	ob3=ch[3]
	ob4=ch[4]
	var flag=ul.children[3].innerText.replace(/\s+/g,"")
		if(flag=="退出")
		{
		  index[3]="quite"
		}

	ob0.onclick=function(){
		mark.value=index[0]
		mark.click()
	}
	ob1.onclick=function(){
		mark.value=index[1]
		mark.click()
	}
	ob2.onclick=function(){
		mark.value=index[2]
		mark.click()
	}
	ob3.onclick=function(){
		mark.value=index[3]
		mark.click()
	}
	ob4.onclick=function(){
		mark.value=index[4]
		mark.click()
	}
}