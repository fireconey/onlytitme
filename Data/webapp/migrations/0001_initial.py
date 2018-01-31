# Generated by Django 2.0 on 2018-01-31 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='webapp.AuthGroup')),
            ],
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('codename', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
                ('last_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='webapp.AuthGroup')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='webapp.AuthUser')),
            ],
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='webapp.AuthPermission')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='webapp.AuthUser')),
            ],
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
                ('action_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='eval',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('img', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=5000)),
                ('good', models.IntegerField()),
                ('bad', models.IntegerField()),
                ('p', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='WebappImg',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('img', models.CharField(max_length=8, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='WebappLoc',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('sheng', models.CharField(blank=True, max_length=8, null=True)),
                ('shi', models.CharField(max_length=8)),
                ('xiang', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='WebappNews',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('content', models.CharField(max_length=10000)),
                ('time', models.IntegerField()),
                ('loc', models.CharField(max_length=30)),
                ('flag', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='WebappShoping',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=10, null=True)),
                ('price', models.CharField(blank=True, max_length=100, null=True)),
                ('needintro', models.CharField(max_length=10000)),
                ('content', models.CharField(max_length=50000)),
                ('loc', models.CharField(max_length=30)),
                ('flag', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='WebappUsr',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('usr', models.CharField(max_length=30, unique=True)),
                ('passwd', models.CharField(max_length=30)),
                ('sex', models.CharField(max_length=10)),
                ('birth', models.CharField(max_length=30)),
                ('wx', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('loc', models.TextField()),
                ('infold', models.TextField(blank=True, null=True)),
                ('img', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='webappshoping',
            name='usr',
            field=models.ForeignKey(db_column='usr', on_delete=django.db.models.deletion.DO_NOTHING, to='webapp.WebappUsr'),
        ),
        migrations.AddField(
            model_name='webappnews',
            name='usr',
            field=models.ForeignKey(db_column='usr', on_delete=django.db.models.deletion.DO_NOTHING, to='webapp.WebappUsr'),
        ),
        migrations.AddField(
            model_name='webappimg',
            name='usr',
            field=models.ForeignKey(db_column='usr', on_delete=django.db.models.deletion.DO_NOTHING, to='webapp.WebappUsr'),
        ),
        migrations.AddField(
            model_name='eval',
            name='usr',
            field=models.ForeignKey(db_column='usr', on_delete=django.db.models.deletion.DO_NOTHING, to='webapp.WebappUsr'),
        ),
        migrations.AddField(
            model_name='djangoadminlog',
            name='content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='webapp.DjangoContentType'),
        ),
        migrations.AddField(
            model_name='djangoadminlog',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='webapp.AuthUser'),
        ),
        migrations.AddField(
            model_name='authpermission',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='webapp.DjangoContentType'),
        ),
        migrations.AddField(
            model_name='authgrouppermissions',
            name='permission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='webapp.AuthPermission'),
        ),
    ]
