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
    ob=0
    mutex.acquire()
    clear()
    if state=="1":

        ob=model.objects.filter(flag=fl)[n:m]
    if state=="2":
        ob = model.objects.filter(flag=fl,loc=local)[n:m]

    number=ob.count()
    print("number",number)
    for i in range(0, number):
        img.append(model2.WebappUsr.objects.get(usr=ob[i].usr.usr).img)
        # print(i,"***",img)
        title.append(ob[i].title)
        content.append(ob[i].content)
        usr.append(ob[i].usr.usr)
    for i in range(number,m):
        img.append("空")
        title.append("无数据")
        content.append("无数据")
        usr.append("空")
    print("img",img)

    pack.clear()
    pack.set(img, "img")
    pack.set(title,"title")
    pack.set(content, "content")
    pack.set(usr, "usr")
    mutex.release()
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





