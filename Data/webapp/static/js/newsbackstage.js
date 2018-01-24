window.onload=function(){
	loadLocal()
	initbody()

}

function loadLocal(){
    new PCAS("province6","city6","area6","湖南省","长沙市","芙蓉区");
}

function initbody(){



	var yes=$("#yes")
	var cancel=$("#cancel")
	yes.getEl(0).onmousedown=function(){
		yes.css("color:#FFF")

	}
	yes.getEl(0).onmouseup=function(){
		yes.css("color:red")
	}

	cancel.getEl(0).onmousedown=function(){
		cancel.css("color:#FFF")
	}
	cancel.getEl(0).onmouseup=function(){
		cancel.css("color:red")
	}


}