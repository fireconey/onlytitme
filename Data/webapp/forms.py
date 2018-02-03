from django import forms
from webapp.models import WebappUsr as umodel
from django.forms import ValidationError
from . import views
flag=0
def usrValidate(value):
    global  flag
    try:
        flag=umodel.objects.get(usr=value)
    except:
        flag=0
    if flag==0:
        raise ValidationError("用户名错误")

def noUsrValidate(value):
    global  flag
    try:
        flag=umodel.objects.get(usr=value)
    except:
        flag=0
    if flag!=0:
        raise ValidationError("已有此用户")

def passwdValidate(value):
    global  flag

    if flag!=0:
        print(value+"hhhhh")
        flag=flag.passwd
        print(flag+"5555")
    print(flag,"22999",value)
    if  flag!=value:
        raise  ValidationError("密码错误")

flag=0
pw=""
def tpasswdValidate(value):
    global flag,pw
    if flag==0:
        pw=value
        flag=1
    else:
        flag=0
        if pw!=value:
            raise  ValidationError("密码不相同")
class Loading(forms.Form):
    usr=forms.CharField(max_length=10,
                        validators=[usrValidate],
                        error_messages={"required":"用户名不能为空"})
    passwd=forms.CharField(max_length=20,
                           validators=[passwdValidate],
                           error_messages={"required":"密码不能为空"})




class Regist(forms.Form):
    img=forms.CharField(max_length=1000)
    usr=forms.CharField(max_length=10,
                          validators=[noUsrValidate],
                          error_messages={"required": "不能为空"})
    passwd =forms.CharField(max_length=20,
                             validators=[tpasswdValidate],
                             error_messages={"required": "不能为空"})
    passwd2=forms.CharField(max_length=20,
                             validators=[tpasswdValidate],
                             error_messages={"required": "不能为空"})
    mw=((0,u"男"),
        (1,u"女"))
    sex=forms.CharField(widget=forms.Select(choices=mw))
    birth=forms.CharField(error_messages={"required": "不能为空"})
    wx=forms.CharField(error_messages={"required": "不能为空"})
    phone=forms.CharField(required=False)
    loc=forms.CharField()

class Usr(forms.Form):
    usr = forms.CharField(max_length=10,
                          validators=[noUsrValidate],
                          error_messages={"required": "不能为空"})




def UsrInfoValidate(value):
    global  flag

    try:
        flag=umodel.objects.get(usr=value)
    except:
        flag=0
    if flag!=0:
        raise ValidationError("已有此用户")


class uinfo(forms.Form):
    img = forms.CharField(max_length=100)
    usr = forms.CharField(max_length=10,
                          validators=[UsrInfoValidate],
                          error_messages={"required": "不能为空"})
    passwd = forms.CharField(max_length=20,
                             error_messages={"required": "不能为空"})

    mw = ((0, u"男"),
          (1, u"女"))
    sex = forms.CharField(widget=forms.Select(choices=mw))
    birth = forms.CharField(error_messages={"required": "不能为空"})
    wx = forms.CharField(error_messages={"required": "不能为空"})
    phone = forms.CharField(required=False)
    loc = forms.CharField()