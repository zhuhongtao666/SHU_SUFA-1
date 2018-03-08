# Generated by Django 2.0.2 on 2018-03-04 01:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='编号')),
                ('title', models.CharField(max_length=20, verbose_name='标题')),
                ('thumb_up', models.PositiveSmallIntegerField(default=0, verbose_name='好评')),
                ('status', models.SmallIntegerField(default=-1, verbose_name='状态')),
            ],
            options={
                'verbose_name': '新闻',
                'verbose_name_plural': '新闻',
                'db_table': 'news',
            },
        ),
        migrations.CreateModel(
            name='NewsPosition',
            fields=[
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False, verbose_name='编号')),
                ('name', models.CharField(max_length=10, verbose_name='名称')),
                ('description', models.CharField(max_length=100, verbose_name='描述')),
                ('status', models.BooleanField(default=True, verbose_name='状态')),
            ],
            options={
                'verbose_name': '新闻板块位置',
                'verbose_name_plural': '新闻板块位置',
                'db_table': 'news_position',
            },
        ),
        migrations.CreateModel(
            name='NewsReviews',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='编号')),
                ('content', models.CharField(max_length=200, verbose_name='评论')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='评论者')),
            ],
            options={
                'verbose_name': '新闻评论',
                'verbose_name_plural': '新闻评论',
                'db_table': 'news_reviews',
            },
        ),
        migrations.CreateModel(
            name='NewsContent',
            fields=[
                ('news', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='news.News', verbose_name='新闻')),
                ('content', models.CharField(max_length=2000, verbose_name='内容')),
            ],
            options={
                'verbose_name': '新闻内容',
                'verbose_name_plural': '新闻内容',
                'db_table': 'news_content',
            },
        ),
        migrations.AddField(
            model_name='newsreviews',
            name='news',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.News', verbose_name='新闻'),
        ),
        migrations.AddField(
            model_name='news',
            name='position',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='news.NewsPosition', verbose_name='板块'),
        ),
        migrations.AddField(
            model_name='news',
            name='writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者'),
        ),
    ]