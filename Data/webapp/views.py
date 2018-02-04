from django.shortcuts import render
from django.http import  HttpResponse
from webapp import models as model
from django.http import HttpResponseRedirect
from .forms import Loading as ldform
from . import forms as form
from django.views.decorators.csrf import csrf_exempt
from urllib import  parse
import os
import  shutil
import  webapp.tool as tool
import threading
import  time
import json



# Create your views here.
#登录检查标记

'''以下为已经开发好了的'''
threadnumber=1

# flag=0
# utemp=0
# initimg="static/img/loading.jpg"
# initusr="姓名"
# iniloc="地关村"
# iny=0
#
# fl=0
# local=0
# tag=0
# title=""
# content=""
# loc=""
# flag2=""
# title=0
# name=0

def timedele():
    global iny,threadnumber
    tim=time.time()*1000
    tyu=model.WebappNews.objects.exclude(time__gte=tim)
    all=tyu.count()
    try:
        tyu.delete()
        for i in range(0,all):
            nes=model.eval.objects.filter(usr=tyu[i].usr,title=tyu[i].title)
            nes.delete()

    except:
        print("$$$$","异常")
    timer=threading.Timer(5,timedele)
    threadnumber=timer
    timer.start()



@csrf_exempt
def index(request):
    global  threadnumber
    ob = "登录"
    rg = "注册"

    if threadnumber==1:
        timer = threading.Timer(2, timedele)
        timer.start()

#从cookie中知道用户的名称和头像及是否登录
    initusr=tool.chinese(request.COOKIES.get("_initusr"))
    initimg=tool.chinese(request.COOKIES.get("_initimg"))
    flag=tool.chinese(request.COOKIES.get("_flag"))
    if initusr=="":
        initusr="姓名"
    if initimg=="":
        initimg="static/img/loading.jpg"
    if flag=="in":
        ob="退出"
        rg="已登录"
    if flag=="out" or flag=="":
        ob="登录"
        initimg = "static/img/loading.jpg"
        initusr = "姓名"

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
    flag=tool.chinese(request.COOKIES.get("_flag"))
    dic = {}
    if flag=="in":
        return HttpResponseRedirect("index")

    initphoto="/static/img/loading.jpg"
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
            initimg=model.WebappUsr.objects.get(usr=u).img
            initusr=u
            response=HttpResponseRedirect("index")
            response.set_cookie("_flag","in")
            response.set_cookie("_initimg",parse.quote(initimg))
            response.set_cookie("_initusr",parse.quote(initusr))


            return response
        else:
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
    response=HttpResponseRedirect("/index")
    response.set_cookie("_flag","out")
    response.set_cookie("_initusr","")
    response.set_cookie("_initimg","")
    return response

"""
1、从数据库中查询数据显示到页面
2、修改数据点击提交修改数据库中的对应数据使用ajax

"""

@csrf_exempt
def userInfo(request):
    ob = "登录"
    rg = "注册"
    flag=tool.chinese(request.COOKIES.get("_flag"))
    initusr=tool.chinese(request.COOKIES.get("_initusr"))
    # 第一次进入时是由于没有flag所以flag置为""
    # 导致点击的头像可以进入这页面
    if flag=="":
        flag="out"
    if flag=="out":
        return HttpResponseRedirect("loading")
    if flag == "in":
        ob = "退出"
        rg = "已登录"

    query=model.WebappUsr
    if request.method=="POST":
        data=request.POST
        try:
            file = request.FILES["file"]
        except:
            print("没有文件上传")
        if data["flag"]=="up":
            utemp=initusr.strip()

            ob = model.WebappUsr.objects.get(usr=initusr)
            ob.img = "static/"+utemp+"/"+file.name
            ob.save()

            ev = model.eval.objects.filter(p=initusr)
            ev.update(img="static/" + utemp + "/" + file.name)

            try:
                shutil.rmtree("webapp/static/"+utemp+"/")
            except:
                print("没有这个目录")
            if not os.path.exists("webapp/static/"+utemp):
                os.mkdir("webapp/static/"+utemp)
            with open("webapp/static/"+utemp+"/"+file.name,"wb+") as f:
                for i in file:
                    f.write(i)
            response=HttpResponse("../static/"+utemp+"/"+file.name)
            response.set_cookie("_initimg",parse.quote("static/"+utemp+"/"+file.name))
            return response

        if  data["flag"]=="change":
            ob = model.WebappUsr.objects.get(usr=initusr)
            ev=model.eval.objects.filter(p=initusr)
            if initusr!=data["usr"]:
                uform = form.uinfo(data)
            else:uform=form.uinfo2(data)

            if uform.is_valid():
                ob.usr=data["usr"]
                ob.sex=data["sex"]
                ob.birth=data["birth"]
                ob.passwd=data["passwd"]
                ob.wx=data["wx"]
                ob.phone=data["phone"]
                ob.loc=data["loc"]
                ob.img="static/"+data["usr"]+"/"+ob.img.split("/")[-1]

                try:
                    shutil.move("webapp/static/"+initusr,"webapp/static/"+data["usr"])
                except:
                    print("第一次没有创建文件的所以不能更名")
                ob.save()
                ev.update(p=data["usr"],img=ob.img)




                response=HttpResponse("temp")
                response.set_cookie("_initusr",parse.quote(ob.usr))
                response.set_cookie("_initimg",parse.quote(ob.img))
                return response
            else:
                er={}
                for i in uform.errors:
                    er[i]=uform.errors[i]
                return  HttpResponse(str(er))

    query = query.objects.filter(usr=initusr)[0]
    eval = model.personeval.objects.filter(usr=query)[0]
    good=eval.goodperson
    bad=eval.badperson
    xinyong=float("%.2f" %((good-bad)*100/(good+bad+1)))
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
                    "img":img,
                    "good":good,
                    "bad":bad,
                    "xinyong":xinyong
                   })
@csrf_exempt
def timenewsdetail(request):
    initusr=tool.chinese(request.COOKIES.get("_initusr"))
    initimg=tool.chinese(request.COOKIES.get("_initimg"))
    name=tool.chinese(request.COOKIES.get("_name"))
    title=tool.chinese(request.COOKIES.get("_title"))
    flag=tool.chinese(request.COOKIES.get("_flag"))
    fl=tool.chinese(request.COOKIES.get("_fl"))
    print(flag,"flag")
    if initusr=="":
        initusr="姓名"
    if initimg=="":
        initimg="static/img/loading.jpg"


    img="#"
    good="无数据"
    bad="无数据"
    goodperson="无数据"
    badperson="无数据"
    personxy="无数据"
    content="无数据"
    phone="无数据"
    wx="无数据"
    xinyong="无数据"
    ob="登录"
    rg = "注册"
    if flag=="in":
        ob="退出"
        rg = "已登录"

    try:
        newsmodel=model.WebappNews.objects.filter(usr=name,title=title,flag=fl)[0:1][0]
        umodel=model.WebappUsr.objects.get(usr=name)
        evalmodel=model.eval.objects.filter(usr=umodel)
        perpri=model.personeval.objects.get(usr=umodel)

        goodperson=perpri.goodperson
        badperson=perpri.badperson

        title=newsmodel.title
        content=newsmodel.content
        phone=umodel.phone
        wx=umodel.wx
        img=umodel.img
        good=evalmodel.filter(evaluate=1).count()
        bad=evalmodel.filter(evaluate=0).count()


        xinyong=float('%.2f' % ((good-bad)*100/(good+bad+1)))
        personxy=float("%.2f" % ((goodperson-badperson)*100/(goodperson+badperson+1)))
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
                    "goodperson":goodperson,
                    "badperson":badperson,
                    "personxy":personxy
                   })


@csrf_exempt
def newsList(request):

    initusr=tool.chinese(request.COOKIES.get("_initusr"))
    initimg=tool.chinese(request.COOKIES.get("_initimg"))
    flag=tool.chinese(request.COOKIES.get("_flag"))
    fl = tool.chinese(request.COOKIES.get("_fl"))#由于flag判断登录
    local=tool.chinese(request.COOKIES.get("_local"))
    tag = tool.chinese(request.COOKIES.get("_tag"))
    search=tool.chinese(request.COOKIES.get("_search"))
    if initusr=="":
        initusr="姓名"
    if initimg=="":
        initimg="static/img/loading.jpg"
    ob = "登录"
    rg = "注册"
    try:
        #按照标签查询，如果查找不到，就全部安装地域查询
        nes=model.WebappNews.objects.filter(loc=local,flag=fl)
        all=nes.count()
        if  all==0:
            all=model.WebappNews.objects.filter(flag=fl).count()
        if all%60!=0:
            all=int(all/60)+1
        else:
            all=all/60
        if all==0:
            all=1  #解决有的页面没有东西，上面的查询导致all=0,的问题


    except:
        all=0

    if flag == 0:
        ob = "登录"
        initimg = "../static/img/loading.jpg"
        initusr = "姓名"
    if flag =="in":
        ob = "退出"
        rg = "已登录"
    if request.method=="POST":
        newsmodel = model.WebappNews
        fro=request.POST["from"]
        if fro=="indexlabel":
            fl=request.POST["flag"]
            local=request.POST["local"]
            tag=request.POST["tag"]
            response=HttpResponse("newslist")
            response.set_cookie("_fl",parse.quote(fl))
            response.set_cookie("_local",parse.quote(local))
            response.set_cookie("_tag",parse.quote(tag))
            return response
        if fro=="indexbar":
            fl=request.POST["flag"]
            local=request.POST["local"]
            tag=request.POST["tag"]
            response = HttpResponse("newslist")
            response.set_cookie("_fl", parse.quote(fl))
            response.set_cookie("_local", parse.quote(local))
            response.set_cookie("_tag", parse.quote(tag))
            return response

        if fro=="newslist":
            count = int(request.POST["count"]) - 1
            ty = tool.query2(newsmodel, 60 * count, 60 * (1 + count),fl,  local, tag).get()
            response= HttpResponse(json.dumps(ty))
            response.set_cookie("al",ty["all"])
            return  response

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



"""
后台
"""
@csrf_exempt
def newsbackstage(request):
    ob="登录"
    rg="注册"
    fla=tool.chinese(request.COOKIES.get("_flag"))
    initusr=tool.chinese(request.COOKIES.get("_initusr"))
    initimg=tool.chinese(request.COOKIES.get("_initimg"))
    title=""
    tag =tool.chinese( request.COOKIES.get("_tag"))
    content=""
    loc=""
    button="发布"
    if fla=="in":
        ob="退出"
        rg="已注册"

    if request.method=="POST":
        rq=request.POST
        if rq["flag"]=="save":  #从发布系统来的
            time=rq["time"]
            flag=rq["select"]
            loc=rq["group"]
            title=rq["title"]
            content=rq["content"]
            usr=model.WebappUsr.objects.get(usr=initusr)
            news=model.WebappNews(title=title,
                                  content=content,
                                  time=time,
                                  loc=loc,
                                  flag=flag,
                                  usr=usr)
            news.save()
            return  HttpResponse("newsbackstage")

        if rq["flag"]=="update":  #从发布系统来的

            time=rq["time"]
            flag=rq["select"]
            loc=rq["group"]
            title=rq["title"]
            odtitle=request.COOKIES.get("_title")


            content=rq["content"]
            usr=model.WebappUsr.objects.get(usr=initusr)
            news=model.WebappNews.objects.filter(usr=usr,title=odtitle)
            news.update(title=title,
                        content=content,
                        time=time,
                        loc=loc,
                        flag=flag,
                        )
            return  HttpResponse("ok")
    if tag=="manager":
        title=tool.chinese(request.COOKIES.get("_title"))
        um=model.WebappUsr.objects.get(usr=initusr)
        news=model.WebappNews.objects.filter(usr=um,title=title)
        content=news[0].content
        loc=news[0].loc
        button="修改"
    response=render(request,"pages/newsbackstage.html",
                                                {
                                                "ob":ob,
                                                "rg":rg,
                                                "title":title,
                                                "content":content,
                                                "loc":loc,
                                                "initimg":initimg,
                                                "initusr":initusr,
                                                "button":button
                                                })
    #由于从管理界面进入后标记了_tag,如果不清除，导致从发布进入的页面
    #就会进入if tag="manager"程序中;
    response.set_cookie("_tag","")
    return response



@csrf_exempt
def file(request):
    initusr=tool.chinese(request.COOKIES.get("_initusr"))
    if initusr=="":
        initusr="姓名"
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
    response=  HttpResponse("static/"+initusr+"/"+file.name)
    response.set_cookie("_initimg","static/"+initusr+"/"+file.name)
    return  response


@csrf_exempt
def info(request):
    ob="登录"
    rg = "注册"
    flag=tool.chinese(request.COOKIES.get("_flag"))
    initimg=tool.chinese(request.COOKIES.get("_initimg"))
    initusr=tool.chinese(request.COOKIES.get("_initusr"))
    if initusr=="":
        initusr="姓名"
    if initimg=="":
        initimg="static/img/loading.jpg"
    if flag=="in":
        ob="退出"
        rg = "已登录"
    if flag=="out":
        return HttpResponseRedirect("loading")
    if request.method=="POST":

        fla=request.POST["flag"]
        if fla=="fill":
            count = int(request.POST["count"])
            title=[]
            utemp=model.WebappUsr.objects.get(usr=initusr)
            news=model.WebappNews.objects.filter(usr=utemp)
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



@csrf_exempt
def eval(request):
    ob="登录"
    rg = "注册"
    flag=tool.chinese(request.COOKIES.get("_flag"))
    if flag=="in":
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
            personprice=model.personeval.objects.filter(usr=name)

            ev=model.eval(img=img,title=title,content=content,evaluate=score,p=p,usr=umoel)
            ev.save()
            if personprice.count() == 0:
                if score==1:
                    model.personeval(usr=umoel, goodperson=score,badperson=0).save()
                else:model.personeval(usr=umoel, goodperson=0,badperson=score).save()
            else:
                if int(score)==1:
                    good=personprice[0].goodperson+int(score)
                    personprice.update(goodperson=good)
                if int(score)==0:
                    bad=personprice[0].badperson+1
                    personprice.update(badperson=bad)


            return HttpResponse("OK")

            
        




    return  render(request,"pages/eval.html",
                   {"ob":ob,
                     "rg":rg

                   })





