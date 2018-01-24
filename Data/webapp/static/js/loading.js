window.onload=function(){
	initbody()
	skip()
	iput()
	lossFocus()

	
}

window.onresize=function(){
	initbody()
}

function initbody()
{
	var h=window.innerHeight
	var ob=document.getElementById("inner")
	var w=ob.offsetWidth
	ob.style.height=w/5.12+"px"
	ob.style.marginTop=(h-w/5.12)/2+"px"
}




//在django中由于添加了{% csrf_token %}导致默认有个input
//正则表达式没有双引号
//onchange是按确定键时才检查
/*
  1、每次按下按键都检查是否有空格，有空格就清除
  2、如果通过检查是否清除了input中的"请"字来决定input的text或者password
     类型。
  3、按了确定键密码也隐藏
*/
function iput(){
	var ob=document.getElementsByTagName('input')
	
	ob[1].onkeyup=function(){
		this.value=this.value.replace(/\s+/g,"")
	}
	ob[2].onkeyup=function(){
		this.value=this.value.replace(/\s+/g,"")
		var v=this.value.search(/请/g)
		if(v==0){
			this.setAttribute("type","text")
		}
		else{
			this.setAttribute("type","password")
		}
	}
	

}

/*
  1、取消键和注册键的跳转
*/

function skip(){
	 var cancel=document.getElementById("cancel")
	 var reg=document.getElementById("reg")
	 cancel.onclick=function(){
	 	window.location.href="index"
	 }
	 reg.onclick=function(){
	 	window.location.href="regist"
	 }

}

function lossFocus(){
	var ob=document.getElementsByTagName("input")
	   ob[1].onfocus=function(){
		     this.value=""
	   }
	   ob[2].onfocus=function(){
			this.value=""
	   }
}










