from django.shortcuts import render
from django.http import  HttpResponse
from webapp import models as model
from django.http import HttpResponseRedirect
from .forms import Loading as ldform
from . import forms as form
from django.views.decorators.csrf import csrf_exempt
import os
import  shutil
import  webapp.tool as tool
import threading
import  time
import json



# Create your views here.
#登录检查标记

'''以下为已经开发好了的'''
flag=0
utemp=0
initimg="static/img/loading.jpg"
initusr="姓名"
iniloc="地关村"
iny=0
threadnumber=1
def timedele():
    global iny,threadnumber
    tim=time.time()*1000
    tyu=model.WebappNews.objects.exclude(time__gte=tim)
    all=tyu.count()
    try:
        for i in range(0,all):
            nes=model.eval.objects.filter(usr=tyu[i].usr,title=tyu[i].title)
            nes.delete()
        tyu.delete()
    except:
        print("$$$$","异常")
    timer=threading.Timer(5,timedele)
    threadnumber=timer
    timer.start()



@csrf_exempt
def index(request):
    global  initusr,initimg,threadnumber
    if threadnumber==1:
        timer = threading.Timer(2, timedele)
        timer.start()
    ob="登录"
    rg="注册"
    if flag==0:
        ob="登录"
        initimg = "static/img/loading.jpg"
        initusr = "姓名"
    if flag==1:
        ob="退出"
        rg="已登录"

    if request.method=="POST":
        rq=request.POST
        if rq["tag"]=="fill":
            newsmodel= model.WebappNews
            result=tool.query(newsmodel,int(rq["n"]),int(rq["m"]),rq["local"],rq["flag"],rq["state"])
            return HttpResponse(json.dumps(result.get()))
        elif rq["tag"]=="qry":
            newsmodel=model.WebappNews
            ob=newsmodel.objects.filter(flag=rq["flag"],loc=rq["local"])[0:15]
            if ob.count()!=0:
                return  HttpResponse(str({"result":1}))
            else:
                return HttpResponse(str({"result":0}))


    return  render(request,"index.html",{"ob":ob,
                                         "rg":rg,
                                         "initusr":initusr,
                                         "initimg":initimg,
                                          "range":range(1,6),

                                         })


@csrf_exempt
def  regist(request):
    global  flag
    if flag==1:
        return HttpResponseRedirect("index")
    dic={}
    initphoto="../static/img/loading.jpg"
    if request.method=="POST":
        file=request.FILES
        usr=request.POST
        umodle=form.Regist(usr)
        onlyu=form.Usr(usr)
        if umodle.is_valid() and usr["flag"]=="submit":
            data=umodle.clean()
            initphoto=data["img"]
            model.WebappUsr(usr=data["usr"],
                            passwd=data["passwd"],
                            sex=data["sex"],
                            birth=data["birth"],
                            wx=data["wx"],
                            phone=data["phone"],
                            loc=data["loc"],
                            img=initphoto
                            ).save()

            return  HttpResponse("temp")
        elif usr["flag"]=="submit":
            for i in umodle.errors:
                dic[i]=umodle.errors.get(i)
            return HttpResponse(str(dic))

        if onlyu.is_valid() and usr["flag"]=="im":
            if not os.path.exists("webapp/static/"+usr["usr"]):
                os.mkdir("webapp/static/"+usr["usr"])
            with open("webapp/static/"+usr["usr"]+"/"+file["file"].name,"wb+") as f:
                for i in file["file"]:
                    f.write(i)
            return HttpResponse("static/"+usr["usr"]+"/"+file["file"].name)
        elif usr["flag"]=="im":
            for i in onlyu.errors:
                dic[i]=onlyu.errors.get(i)
            return  HttpResponse(str(dic))
        elif usr["flag"]=="cancel":
            shutil.rmtree("webapp/static/" + usr["ucancel"])
            return HttpResponse("ok")

    else:
        obj=form.Regist()
        return  render(request,"pages/regist.html",{"im":initphoto,
                                                    "obj":obj})


def  loading(request):
    global  flag,utemp,initusr,initimg
    t = True  #获取的密码是『请输入密码』的标记
    if request.method=="POST":
        r = request.POST

        #由于每次获取时都莫名其妙的有空格所以再
        #同时在html有的语句不支持如（strip）所以
        #处理好之后导入数据
        pw = r["passwd"].strip()
        u=r["usr"].strip()
        #导入数据到表单中便于验证
        obj=ldform(r)

        #验证通过就到首页
        if obj.is_valid():
            data=obj.clean()
            flag=1
            initimg=model.WebappUsr.objects.get(usr=u).img
            utemp=u
            initusr=utemp
            return  HttpResponseRedirect("/index")
        else:
            flag=0
            if pw!="请输入密码":
                t=False
            else:
                t=True
            return render(request,"pages/loading.html",
                  {"obj":obj,
                  "u":u,
                  "b":t,
                  "pw":pw})
    else:
        obj=ldform()
        return  render(request,"pages/loading.html",{"obj":obj,
                 "b":t,
                 "u":"请输入账号",
                 "pw":"请输入密码"})


def quite(request):
    global flag
    flag=0
    return  HttpResponseRedirect("/index")

"""
1、从数据库中查询数据显示到页面
2、修改数据点击提交修改数据库中的对应数据使用ajax

"""

@csrf_exempt
def userInfo(request):

    global  utemp,initimg,initusr
    if flag==0:
        return HttpResponseRedirect("loading")
    ob = "登录"
    rg = "注册"
    query=model.WebappUsr
    usr=""
    sex=""
    birth=""
    passwd=""
    wx=""
    phone=""
    loc=""
    img=""
    # if flag==0:
    #     return  HttpResponseRedirect("index")
    if flag == 1:
        ob = "退出"
        rg = "已登录"
    if request.method=="POST":
        data=request.POST
        try:
            file = request.FILES["file"]
        except:
            print("没有文件上传")
        if data["flag"]=="up":
            ob = model.WebappUsr.objects.get(usr=utemp)
            ev=model.eval.objects.filter(p=utemp)


            ob.img = "static/"+data["usr"]+"/"+file.name
            initimg = "static/"+data["usr"]+"/"+file.name
            ob.save()
            ev.update(img="static/" + data["usr"] + "/" + file.name)



            try:
                shutil.rmtree("webapp/static/"+data["usr"])
            except:
                print("没有这个目录")
            if not os.path.exists("webapp/static/"+data["usr"]):
                os.mkdir("webapp/static/"+data["usr"])
            with open("webapp/static/"+data["usr"]+"/"+file.name,"wb+") as f:
                for i in file:
                    f.write(i)
            return  HttpResponse("../static/"+data["usr"]+"/"+file.name)

        if  data["flag"]=="change":
            ob = model.WebappUsr.objects.get(usr=utemp)
            ev=model.eval.objects.filter(p=utemp)
            uform = form.uinfo(data)
            if uform.is_valid():
                ob.usr=data["usr"]
                ob.sex=data["sex"]
                ob.birth=data["birth"]
                ob.passwd=data["passwd"]
                ob.wx=data["wx"]
                ob.phone=data["phone"]
                ob.loc=data["loc"]
                ob.img="static/"+data["usr"]+"/"+ob.img.split("/")[-1]
                ev.update(img=ob.img)
                initusr=ob.usr
                initimg=ob.img
                try:
                    shutil.move("webapp/static/"+utemp,"webapp/static/"+data["usr"])
                except:
                    print("第一次没有创建文件的所以不能更名")
                utemp = data["usr"]
                ob.save()
                utemp = data["usr"]
                return HttpResponse("temp")
            else:
                er={}
                for i in uform.errors:
                    er[i]=uform.errors[i]
                return  HttpResponse(str(er))


    try:
        query = query.objects.get(usr=utemp)
        usr = query.usr
        sex = query.sex
        if int(sex)==0:
            sex="男"
        elif int(sex)==1:
            sex="女"
        birth = query.birth
        passwd = query.passwd
        wx = query.wx
        phone = query.phone
        loc = query.loc
        img=query.img

        utemp = usr
    except:
        print("查询有错误")
    return  render(request,"pages/uinfo.html",
                   {"ob":ob,
                     "rg":rg,
                    "usr":usr,
                    "sex":sex,
                    "birth":birth,
                    "passwd":passwd,
                    "wx":wx,
                    "phone":phone,
                    "loc":loc,
                    "img":img
                   })
@csrf_exempt
def timenewsdetail(request):
    global title,name,initusr,initimg
    img="#"
    good="无数据"
    bad="无数据"
    content="无数据"
    phone="无数据"
    wx="无数据"
    xinyong="无数据"
    ob="登录"
    rg = "注册"
    if flag==1:
        ob="退出"
        rg = "已登录"
    if request.method=="POST":
        title=request.POST["title"].strip()
        name=request.POST["name"].strip()
        return  HttpResponse("timenewsdetail")
    try:
        newsmodel=model.WebappNews.objects.filter(usr=name,title=title)[0:1][0]
        umodel=model.WebappUsr.objects.get(usr=name)
        evalmodel=model.eval.objects.filter(usr=name)
        title=newsmodel.title
        content=newsmodel.content
        phone=umodel.phone
        wx=umodel.wx
        img=umodel.img
        good=evalmodel.filter(evaluate=1).count()
        bad=evalmodel.filter(evaluate=0).count()
        xinyong=float('%.2f' % ((good-bad)*100/(good+bad+1)))
    except:
        pass
    return  render(request, "pages/timenewsdetail.html",
                   {"ob":ob,
                     "rg":rg,
                    "title":title,
                    "content":content,
                    "phone":phone,
                    "wx":wx,
                    "img":img,
                    "bad":bad,
                    "good":good,
                    "xinyong":xinyong,
                    "name":name,
                    "initimg":initimg,
                    "initusr":initusr,
                   })

fl=0
local=0
tag=0
@csrf_exempt
def newsList(request):
    global initusr, initimg,fl,local,tag
    ob = "登录"
    rg = "注册"
    try:
        all=model.WebappNews.objects.all().count()
        if all%60!=0:
            all=int(all/60)+1

    except:
        all=0

    if flag == 0:
        ob = "登录"
        initimg = "../static/img/loading.jpg"
        initusr = "姓名"
    if flag == 1:
        ob = "退出"
        rg = "已登录"
    if request.method=="POST":
        newsmodel = model.WebappNews
        fro=request.POST["from"]
        if fro=="indexlabel":
            fl=request.POST["flag"]
            local=request.POST["local"]
            tag=request.POST["tag"]
            return HttpResponse("newslist")
        if fro=="indexbar":
            fl=request.POST["flag"]
            local=request.POST["local"]
            tag=request.POST["tag"]
            return HttpResponse("newslist")

        if fro=="newslist":
            count = int(request.POST["count"]) - 1
            ty = tool.query2(newsmodel, 60 * count, 60 * (1 + count), fl, local, tag).get()
            return HttpResponse(json.dumps(ty))

    return render(request,"pages/newslist.html",
                  {"range":range(1,21),
                   "ob":ob,
                   "rg":rg,
                   "initusr":initusr,
                   "initimg":initimg,
                   "all":all,
                   "tag":local,
                   "value":fl,
                   })



'''********************以下为有待替换的处理函数************'''
title=""
content=""
loc=""
flag2=""

@csrf_exempt
def newsbackstage(request):
    global title,content,loc,flag2,flag,initimg,initusr
    ob = "登录"
    rg = "注册"
    if flag == 0:
       return HttpResponseRedirect("index")
    if flag == 1:
        ob = "退出"
        rg = "已登录"
    if request.method=="POST":
        result=request.POST
        if result["flag"]=="param":
            title = result["title"]
            news=model.WebappNews.objects.filter(title=title)[0:1]
            content=news[0].content
            loc=news[0].loc
            flag2=news[0].flag
    
        if result["flag"]=="update" and not initusr=="姓名":
           news=model.WebappNews.objects.filter(title=title)
           news.update(
            usr=model.WebappUsr.objects.get(usr=initusr),time=result["time"],
            flag=result["select"],loc=result["group"],title=result["title"],
            content=result["content"])
           title =result["title"]
           content=result["content"]
        return HttpResponse("newsbackstage")
    return  render(request,"pages/newsbackstage.html",{
                 "title":title,"content":content,"loc":loc,
                 "flag":flag2,"initusr":initusr,"initimg":initimg,
                 "ob":ob,
                 "rg":rg,
                 "button":"修改"

                                        })

@csrf_exempt
def newsbackstage2(request):
    global flag,initimg,initusr
    ob = "登录"
    rg = "注册"
    if flag == 0:
        return HttpResponseRedirect("index")
    if flag == 1:
        ob = "退出"
        rg = "已登录"
    title=""
    content=""
    loc=""
    if request.method=="POST":
        result = request.POST
        if result["flag"]=="save" and not initusr=="姓名":
                news=model.WebappNews(usr=model.WebappUsr.objects.get(usr=initusr),time=result["time"],
                flag=result["select"],loc=result["group"],title=result["title"],content=result["content"])
                news.save()
                return HttpResponse("newsbackstage2")
    return  render(request,"pages/newsbackstage.html",{
                 "title":title,"content":content,"loc":loc,
                 "flag":flag2,"initusr":initusr,"initimg":initimg,
                 "ob":ob,
                 "rg":rg,
                 "button":"发布"
                 })


@csrf_exempt
def file(request):
    global initusr
    if request.method=="POST":
        try:
            file=request.FILES["file"]
        except:
            return HttpResponse("falise")
        if not os.path.exists("webapp/static/" +initusr) and initusr!="姓名":
            os.mkdir("webapp/static/" +initusr)
        with open("webapp/static/" + initusr + "/" + file.name, "wb+") as f:
            for i in file:
                f.write(i)
    return  HttpResponse("static/"+initusr+"/"+file.name)





@csrf_exempt
def info(request):
    ob="登录"
    rg = "注册"
    if flag==1:
        ob="退出"
        rg = "已登录"
    if flag==0:
        return HttpResponseRedirect("loading")
    if request.method=="POST":

        fla=request.POST["flag"]
        if fla=="fill":
            count = int(request.POST["count"])
            title=[]
            time=[]
            news=model.WebappNews.objects.filter(usr=initusr)
            all=news.count()
            n=0
            m=0
            if all%10!=0:
                all=(int(all/10)+1)*10
                n=all-count*10
                m = all - (count - 1) * 10
            if n<0 or m<0:
                n=0
                m=0
            news=news[n:m]
            for i in range(0,news.count()):
                title.append(news[i].title)
                # time.append(news[i].time)
            return  HttpResponse(str({"title":title,"all":all}))
        if fla=="content":
            news=model.WebappNews.objects.filter(title=request.POST["title"])[0:1]
            return  HttpResponse(news[0].content)
        if fla=="delet":
            title=request.POST["title"]
            news=model.WebappNews.objects.filter(title=title).delete()
            return HttpResponse("info")




    return  render(request,"pages/info.html",
                   {"ob":ob,
                     "rg":rg,
                    "img":initimg,
                    "usr":initusr

                   })


title=0
name=0
@csrf_exempt


def eval(request):
    ob="登录"
    rg = "注册"
    if flag==1:
        ob="退出"
        rg = "已登录"
    if request.method=="POST":
        result=request.POST
        if result["flag"]=="fill" and not result["usr"]=="姓名":
            title=result["title"]
            usr=result["usr"]
            news=model.eval.objects.filter(usr=usr,title=title)
            all=news.count()
            name=[]
            content=[]
            img=[]
            dic={}

            for i in range(0,all):
                name.append(news[i].p)
                content.append(news[i].content)
                img.append(news[i].img)
            dic["name"]=name
            dic["content"]=content
            dic["img"]=img
            return  HttpResponse(json.dumps(dic))

        def goodbad(value):
            title=result["title"]
            usr=result["usr"]
            news=model.eval.objects.filter(usr=usr,title=title,evaluate=value)
            all=news.count()
            name=[]
            content=[]
            img=[]
            dic={}
            for i in range(0,all):
                name.append(news[i].p)
                content.append(news[i].content)
                img.append(news[i].img)
            dic["name"]=name
            dic["content"]=content
            dic["img"]=img
            return HttpResponse(json.dumps(dic))

        if result["flag"]=="good" and not result["usr"]=="姓名":
           return goodbad(1)

        if result["flag"]=="bad" and not result["usr"]=="姓名": 
           return goodbad(0)    
        if result["flag"]=="save" and not result["usr"]=="姓名":
            p=result["p"]
            name=result["usr"]
            title=result["title"]
            content=result["content"]
            score=result["score"]
            img=result["img"]
            umoel=model.WebappUsr.objects.get(usr=name)
            ev=model.eval(img=img,title=title,content=content,evaluate=score,p=p,usr=umoel)
            ev.save()
            return HttpResponse("OK")

            
        




    return  render(request,"pages/eval.html",
                   {"ob":ob,
                     "rg":rg

                   })


def infodetail(request):
    return render(request,"pages/infodetail.html")





def t(request):
    m=model.WebappNews.objects.filter(flag="3",loc="*")
    print(m.count(),90000000)
    return  HttpResponse("hao")



