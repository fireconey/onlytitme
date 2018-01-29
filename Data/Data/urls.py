"""Data URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from webapp import views  as view

urlpatterns = {
    url('admin/', admin.site.urls),
    url("^index$", view.index),
    url("^regist$", view.regist),
    url("^loading$", view.loading),
    url("^newsbackstage2$",view.newsbackstage2),
    url("^userInfo$",view.userInfo),
    url("^info$",view.info),
    url("^quite$",view.quite),
    url("^eval$",view.eval),
    url("^$",view.index),
    url("^newslist$",view.newsList),
    url("^file$",view.file),
    url("^newsbackstage$",view.newsbackstage),

    #**************************以下为待开发区
    # url("^")

     url("tu",view.t),

    url("^yu$",view.infodetail),
    url("^timenewsdetail$",view.timenewsdetail),
    url("^op$",view.timenewsdetail),

}
