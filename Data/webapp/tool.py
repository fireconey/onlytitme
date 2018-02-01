from . import models as model2
import threading
mutex=threading.Lock()

class pack():
    dic = {}
    def __init__(self):
        self.dic={}
    def set(self, value, key):
        self.dic[key] =value
    def get(self):
        return self.dic
    def clear(self):
        self.dic={}



img=[]
title=[]
goodsphoto=[]
content=[]
price=[]
loc=[]
flag=[]
usr=[]
def clear():
    global  img,content,loc,flag,usr,goodsphoto,price,title
    img=[]
    content = []
    loc = []
    flag = []
    usr = []
    goodsphoto = []
    price=[]
    title=[]

pack=pack()
'''
model：表示具体表的模型
n,m:表示要截取的数据
local：表示要查询的地区
'''
def query(model,n,m,local,fl,state):
    global pack ,img ,content,loc,usr,flag,title
    img=[]
    ob = 0
    def baoz(n1,n2,n3,n4):
        mutex.acquire()
        for i in range(n1, n2):
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
        pack.clear()
        pack.set(img, "img")
        pack.set(title, "title")
        pack.set(content, "content")
        pack.set(usr, "usr")
        mutex.release()
    clear()
    if state=="1":
        ob=model.objects.filter(flag=fl)
        number=ob.count()
        if number>(m-n):
            ob=ob[number-(m-n):number]
            baoz(0,15,0,0)
        if number<(m-n):
            ob=ob[0:number]
            baoz(0,number,number,(m-n))

    if state=="2":
        ob = model.objects.filter(flag=fl,loc=local)
        number = ob.count()
        if number > (m - n):
            ob = ob[number - (m - n):number]
            baoz(0, (m - n), 0, 0)
        if number < (m - n):
            ob = ob[0:m - n]
            baoz(0, number, number, (m - n))
    return pack


def query2(model,n,m,fl,local,tag):
    global pack ,img ,content,loc,usr,flag,title
    clear()
    ob=0
    if tag=="1":
        ob=model.objects.filter(flag=fl)[n:m]
    else:
        ob=model.objects.filter(flag=fl,loc=local)[n:m]
    number=ob.count()
    for i in range(0, number):
        img.append(model2.WebappUsr.objects.get(usr=ob[i].usr.usr).img)
        title.append(ob[i].title)
        content.append(ob[i].content)
        usr.append(ob[i].usr.usr)
    for i in range(number,m):
        img.append("#")
        title.append("无数据")
        content.append("无数据")
        usr.append("空")
    pack.clear()
    pack.set(img, "img")
    pack.set(title,"title")
    pack.set(content, "content")
    pack.set(usr, "usr")
    return pack





