# Generated by Django 2.1.4 on 2019-09-11 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0007_auto_20190911_1754'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='readnum',
            name='topic',
        ),
        migrations.DeleteModel(
            name='ReadNum',
        ),
    ]
