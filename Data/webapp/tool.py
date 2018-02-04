from . import models as model2
from urllib import  parse
import threading
mutex=threading.Lock()

class packob():
    dic = {}
    def __init__(self):
        self.dic={}
    def set(self, value, key):
        self.dic[key] =value
    def get(self):
        return self.dic






'''
model：表示具体表的模型
n,m:表示要截取的数据
local：表示要查询的地区
'''
def query(model,n,m,local,fl,state):
    img = []
    title = []
    content = []
    usr = []
    pack =packob()
    ob = 0

    def baoz(n1,n2,n3,n4):
        for i in range(n1, n2,-1):
            u = ob[i].usr.usr
            img.append(model2.WebappUsr.objects.get(usr=u).img)
            title.append(ob[i].title)
            content.append(ob[i].content)
            usr.append(ob[i].usr.usr)

        for i in range(n3, n4):
            img.append("空")
            title.append("无数据")
            content.append("无数据")
            usr.append("空")

        pack.set(img, "img")
        pack.set(title, "title")
        pack.set(content, "content")
        pack.set(usr, "usr")


    if state=="1":
        ob=model.objects.filter(flag=fl)
        number=ob.count()
        if number>(m-n):
            ob=ob[number-(m-n):number]
            baoz(14,-1,0,0)
        if number<(m-n):
            ob=ob[0:number]
            baoz(number-1,-1,number,(m-n))

    if state=="2":
        ob = model.objects.filter(flag=fl,loc=local)
        number = ob.count()

        if number > (m - n):
            ob = ob[number - (m - n):number]
            baoz(0, (m - n), 0, 0)
        if number < (m - n):
            ob = ob[0:m - n]
            baoz(number-1, -1, number, (m - n))
    return pack


def query2(model,n,m,fl,local,tag):
    img = []
    title = []
    content = []
    usr = []
    pack = packob()
    if tag=="1":
        ob = model.objects.order_by("-time")
        ob=ob.filter(flag=fl)
    else:
        ob=model.objects.order_by("-time")
        ob=ob.filter(flag=fl,loc=local)
    number=ob.count()
    all=number%60
    if not all==0:
        all=int(number/60)+1
    else:
        all=number/60
    if number==0:
        all=1

    if m<number:
        for i in range(n,m):#由于第一个取，第二个不屈，现在是倒序所以要number，0都-1
            img.append(model2.WebappUsr.objects.get(usr=ob[i].usr.usr).img)
            title.append(ob[i].title)
            content.append(ob[i].content)
            usr.append(ob[i].usr.usr)
    else:
        for i in range(n,number):#由于第一个取，第二个不屈，现在是倒序所以要number，0都-1
            img.append(model2.WebappUsr.objects.get(usr=ob[i].usr.usr).img)
            title.append(ob[i].title)
            content.append(ob[i].content)
            usr.append(ob[i].usr.usr)
        for i in range(number,m):
            img.append("#")
            title.append("无数据")
            content.append("无数据")
            usr.append("空")
    pack.set(img, "img")
    pack.set(title,"title")
    pack.set(content, "content")
    pack.set(usr, "usr")
    pack.set(all,"all")
    return pack




def chinese(value):
    if value==None:
       value=""
       return  value
    if not value==None:
        return parse.unquote(value)
