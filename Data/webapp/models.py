# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)




class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)



class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)




class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    last_name = models.CharField(max_length=150)



class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)




class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)



class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()




class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)



class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()



class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()




class WebappImg(models.Model):
    id = models.IntegerField(primary_key=True)
    img = models.CharField(unique=True, max_length=8)
    usr = models.ForeignKey('WebappUsr', models.DO_NOTHING, db_column='usr')



class WebappLoc(models.Model):
    id = models.IntegerField(primary_key=True)
    sheng = models.CharField(max_length=8, blank=True, null=True)
    shi = models.CharField(max_length=8)
    xiang = models.CharField(max_length=8)




class WebappNews(models.Model):
    id = models.IntegerField(primary_key=True)
    usr = models.ForeignKey('WebappUsr', models.DO_NOTHING, db_column='usr')
    title = models.CharField(max_length=500, blank=True, null=True)
    content = models.CharField(max_length=10000)
    time=models.IntegerField()
    loc = models.CharField(max_length=30)
    flag=models.IntegerField()
   




class WebappShoping(models.Model):
    id = models.IntegerField(primary_key=True)
    usr = models.ForeignKey('WebappUsr', models.DO_NOTHING, db_column='usr')
    title = models.CharField(max_length=10, blank=True, null=True)
    price = models.CharField(max_length=100, blank=True, null=True)
    needintro=models.CharField(max_length=10000)
    content = models.CharField(max_length=50000)
    loc = models.CharField(max_length=30)
    flag = models.CharField(max_length=10)






class WebappUsr(models.Model):
    id = models.IntegerField(primary_key=True)
    usr = models.CharField(unique=True, max_length=30)
    passwd = models.CharField(max_length=30)
    sex = models.CharField(max_length=10)
    birth = models.CharField(max_length=30)
    wx = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    loc = models.TextField()
    infold = models.TextField(blank=True, null=True)
    img = models.CharField(max_length=30)

class eval(models.Model):
    id=models.IntegerField(primary_key=True)
    usr=models.ForeignKey("WebappUsr",models.DO_NOTHING,db_column="usr")
    img=models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content=models.CharField(max_length=5000)
    evaluate=models.IntegerField()
    p=models.CharField(max_length=30)

class personeval(models.Model):
    id=models.IntegerField(primary_key=True)
    usr=models.ForeignKey("WebappUsr",models.DO_NOTHING,db_column="usr")
    goodperson=models.IntegerField()
    badperson=models.IntegerField()

