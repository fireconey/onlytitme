window.onload=function(){
	initbody()
	upimg()
	changephoto()
    loadLocal()
    submit()


}


window.onresize=function(){
	initbody()
}
function initbody(){
	var ob=document.getElementById("container")
	var h=window.innerHeight
	ob.style.marginTop=(h-ob.offsetHeight)/2+"px"
	var img=document.getElementById("changephoto")
	var hg=img.offsetHeight
	img.style.width=hg+"px"

}

function upimg(){
	var ob=document.getElementById("file")
	var photo=document.getElementById("photo")
	var chang=document.getElementById("changephoto")
	photo.onclick=function(){
		var ob=document.getElementById("file")
		ob.click()
		chang.style.display="block"
		chang.style.width=chang.offsetHeight+"px"
		this.style.display="none"
		window.setTimeout(function(){
         chang.style.display="block"
		},1500)
	}

}

function changephoto() {
    var change = document.getElementById("changephoto")
    var usr=document.getElementById("usr")

    change.onclick = function () {
        var usrvalue=usr.value.replace(/\s+/g,"")
        if(usrvalue=="不能为空")
        {
            alert("请修改用户名称")
            change.style.display = "none"
            photo.style.display = "block"
            return "null"
        }

        var ob = document.getElementById("file")
        var v = ob.files[0]
        var data = new FormData()
        data.append("file", v)
        data.append("usr",usr.value.replace(/\s+/g,""))
        data.append("flag","im")
        if (window.XMLHttpRequest) {
            xl = new XMLHttpRequest()
        }
        else {
            xl = new ActiveXObject("Microsoft.XMLHTTP")
        }
        xl.onreadystatechange = function () {
            if (xl.readyState == 4 & xl.status == 200) {
                // photo.setAttribute("src",xl.responseText)
                var dic=xl.responseText.replace(/\'+/g,'"').replace(/\[|\]/g,"").replace(/\s+/g,"")
                var h=0
                try{
                    h=JSON.parse(dic)
                }catch(e){
                    h=0
                }
                if(h!=0)
                {
                        var ob=document.getElementById("usr")
                            ob.value=h["usr"]
                            ob.style.color="red"
                            ob.onfocus=function(){
                                //由于循环后最后的为一个确定数。所以用this
                                //每个对象的调取是最后调取的，每次查询的
                                //是查询最后的ob所以使用this
                                this.style.color="yellow"
                                this.value=""
                            }

                }
                else{
                    var ob=document.getElementsByTagName("img")[0]
                        ob.setAttribute("src",dic)
                    // window.location.href="/loading"
                }
                change.style.display = "none"
                photo.style.display = "block"
                photo.style.width = photo.offsetHeight + "px"
            }
        }
        xl.open("post", "regist", true)
        xl.send(data)
    }
}

function loadLocal(){
    new PCAS("province6","city6","area6","湖南省","长沙市","芙蓉区");
}




function submit(){
    var img= document.getElementById("photo")
    var usr=document.getElementById("usr")
    var passwd=document.getElementById("passwd")
    var passwd2=document.getElementById("passwd2")
    var sex=document.getElementById("sex")
    var birth = document.getElementById("birth");
    var wx = document.getElementById("wx");
    var phone = document.getElementById("phone");
    var loc=document.getElementById("loc")
    var group=document.getElementById("group")
    var yes=document.getElementById("yes")
    var cancel=document.getElementById("cancel")

     if (window.XMLHttpRequest) {
            xl = new XMLHttpRequest()
        }
        else {
            xl = new ActiveXObject("Microsoft.XMLHTTP")
        }
    yes.onclick = function () {
        var linkloc=loc.children[0].value+","+loc.children[1].value+","+loc.children[2].value+","+group.value
        var data = new FormData()
        img=img.attributes["src"].value
        data.append("usr",usr.value.replace(/\s+/g,""))
        data.append("passwd", passwd.value.replace(/\s+/g,""))
        data.append("passwd2", passwd2.value.replace(/\s+/g,""));
        data.append("sex",sex.value.replace(/\s+/g,""))
        data.append("birth",birth.value.replace(/\s+/g,""))
        data.append("wx",wx.value.replace(/\s+/g,""))
        data.append("phone",phone.value.replace(/\s+/g,""))
        data.append("loc",linkloc.replace(/\s+/g,""))
        data.append("img",img.replace(/\s+/g,""))
        data.append("flag","submit")


        xl.onreadystatechange = function () {
            if (xl.readyState == 4 & xl.status == 200) {
                // photo.setAttribute("src",xl.responseText)
                var dic=xl.responseText.replace(/\'+/g,'"').replace(/\[|\]/g,"").replace(/\s+/g,"")
                var h=0
                try{
                    h=JSON.parse(dic)
                }catch(e){
                    h=0
                }
                if(h!=0)
                {
                    for(var i in h) 
                    {
                        if (h[i]=="img")
                        {continue}
                        var ob = document.getElementById(i)
                        ob.value = h[i]
                        ob.style.color = "red"
                        ob.onfocus = function () {
                            //由于循环后最后的为一个确定数。所以用this
                            //每个对象的调取是最后调取的，每次查询的
                            //是查询最后的ob所以使用this
                            this.style.color = "yellow"
                            this.value=""
                        }
                    }
                }
                else{

                    window.location.href="/loading"
                }

            }
        }
        xl.open("post", "regist", true)
        xl.send(data)
    }

    cancel.onclick=function (){
        usr=usr.value.replace(/\s+/g,"")
        if (usr=="已有此用户" | usr=="" | usr=="不能为空")
        {
            window.location.href="index"
            return "temp"
        }
        var data=new FormData()
        data.append("flag","cancel")
        data.append("ucancel",usr)
        xl.open("post","regist",true)
        xl.send(data)
        window.location.href="index"

    }
}
