# Generated by Django 2.0.2 on 2018-03-08 14:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('date_joined', models.DateField(auto_created=True, verbose_name='加入社团时间')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.CharField(max_length=8, primary_key=True, serialize=False, verbose_name='学号')),
                ('name', models.CharField(max_length=50, verbose_name='姓名')),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], default='female', max_length=5, verbose_name='性别')),
                ('mobile', models.CharField(max_length=11, unique=True, verbose_name='电话')),
                ('campus', models.CharField(choices=[('BS', '宝山'), ('YC', '延长'), ('JD', '嘉定')], default='BS', max_length=2, verbose_name='校区')),
                ('favorite_club', models.CharField(max_length=20, verbose_name='喜爱的球队')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='member/', verbose_name='证件照')),
                ('is_admin', models.BooleanField(default=False, verbose_name='是否是社团骨干')),
                ('is_active', models.BooleanField(default=False, verbose_name='是否激活')),
                ('is_auth', models.BooleanField(default=False, verbose_name='是否认证')),
            ],
            options={
                'verbose_name': '社团成员信息',
                'verbose_name_plural': '社团成员信息',
                'db_table': 'members',
            },
        ),
        migrations.CreateModel(
            name='MembersClasses',
            fields=[
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='成员')),
                ('monday', models.PositiveSmallIntegerField(default=0, verbose_name='周一课程')),
                ('tuesday', models.PositiveSmallIntegerField(default=0, verbose_name='周二课程')),
                ('wednesday', models.PositiveSmallIntegerField(default=0, verbose_name='周三课程')),
                ('thursday', models.PositiveSmallIntegerField(default=0, verbose_name='周四课程')),
                ('friday', models.PositiveSmallIntegerField(default=0, verbose_name='周五课程')),
            ],
            options={
                'verbose_name': '社团成员课程时间',
                'verbose_name_plural': '社团成员课程时间',
                'db_table': 'members_classes',
            },
        ),
    ]
