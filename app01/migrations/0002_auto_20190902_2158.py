# Generated by Django 2.1.4 on 2019-09-02 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopicType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=16, verbose_name='分类名称')),
            ],
        ),
        migrations.AddField(
            model_name='topic',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app01.User'),
        ),
        migrations.AddField(
            model_name='user',
            name='introduction',
            field=models.TextField(blank=True, null=True, verbose_name='简介'),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=16, null=True, verbose_name='密码'),
        ),
        migrations.AddField(
            model_name='user',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/', verbose_name='头像'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='t_content',
            field=models.TextField(max_length=30, verbose_name='正文'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='t_title',
            field=models.CharField(max_length=30, unique=True, verbose_name='标题'),
        ),
        migrations.AddField(
            model_name='topic',
            name='t_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app01.TopicType'),
        ),
    ]
