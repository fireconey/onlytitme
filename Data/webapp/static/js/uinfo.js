window.onload=function(){
    initbody()
	img();
    topbar()
	changephoto()
	changedata()
}
window.onresize=function(){
	initbody()
}

function initbody(){
	var ob=document.getElementById('inner')
	var w=ob.offsetWidth
	    ob.style.height=w/0.79588+"px"

	var im=document.getElementById("im")
	    im.style.height=im.offsetWidth+"px"

	var headp=document.getElementById("headp")
	    headp.style.width=headp.offsetHeight+"px"

	var fosubmit=document.getElementById("fosubmit")
		fosubmit.onmousedown=function(){

        	fosubmit.style.color="red"


	}
	window.onmouseup=function(){

		fosubmit.style.display="block"
	}

	   

	
}


function img(){
	var ob=document.getElementsByName("mark")[0];
	var img=document.getElementById("headp");
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

function changephoto(){
	var photo=document.getElementById("photo")
	var headp=document.getElementById("headp")
	var submit=document.getElementById("submit")
	var usr=document.getElementById("usr")
	if(window.XMLHttpRequest)
	{
		xl=new XMLHttpRequest()
	}
	else
	{
		xl=new ActiveXObject("Microsoft.XMLHTTP")
	}


	photo.onclick=function(){
		file.click ()
		photo.style.display="none"
		submit.style.display="block"
	}
	submit.onclick=function(){
		var file=document.getElementById("file").files[0]

		this.style.display="none"
		photo.style.display="block"
		var data=new FormData()
        data.append("img",photo.attributes["src"].value)
		data.append("file",file)
		data.append("usr",usr.value.replace(/\s+/,""))
		data.append("flag","up")
		xl.open("post","userInfo",true)
		xl.send(data)
		xl.onreadystatechange=function () {
		if(xl.readyState==4&xl.status==200)
		{
			photo.setAttribute("src",xl.responseText)
			headp.setAttribute("src",xl.responseText)
		}

    }
	}
}


function changedata(){
	if(window.XMLHttpRequest){
		xl=new XMLHttpRequest()
	}
	else{
		xl=new ActiveXObject("Microsoft.XMLHTTP")
	}
    var img=document.getElementById("photo")
	var usr=document.getElementById("usr")
	var sex=document.getElementById("sex")
	var birth=document.getElementById("birth")
	var passwd=document.getElementById("passwd")
	var wx=document.getElementById("wx")
	var phone=document.getElementById("phone")
	var loc=document.getElementById("loc")
    
	var fosubmit=document.getElementById("fosubmit")
     usr.onfocus=function(){
	    this.value=""
     }

    if(sex.value.replace(/\s+/g,"")=="男")
    {
    	sex=0
    }
    else{sex=1}
    fosubmit.onclick=function(){
		if(usr.value.replace(/\s+/g,"")=="已有此用户"|"不能为空")
          {
            return "1"
          }
          if(usr.value.replace(/\s+/g,"")=="不能为空")
          {
            return "1"
          }
    data=new FormData()
    data.append("img",img.attributes["src"].value)
    data.append("usr",usr.value.replace(/\s+/g,""))
    data.append("sex",sex)
    data.append("birth",birth.value.replace(/\s+/g,""))
    data.append("passwd",passwd.value.replace(/\s+/g,""))
    data.append("wx",wx.value.replace(/\s+/g,""))
    data.append("phone",phone.value.replace(/\s+/g,""))
   	data.append("loc",loc.value.replace(/\s+/g,""))
    data.append("flag","change")
    	xl.open("post","userInfo",true)
    	xl.send(data)

    
    xl.onreadystatechange=function(){
    	if(xl.readyState==4&xl.status==200)
    	{   
    		var data=xl.responseText.replace(/\[|\]/g,"").replace(/\'/g,'"')
    		if (xl.responseText!=="temp")
               {
                  data=JSON.parse(data)
				   for(var i in data)
				   {
				   	   var ob=document.getElementById(i)
					   ob.value=data[i]
				   }

               }
               else {
    		    window.location.href="/userInfo"
            }

    	}
    }
    }
}