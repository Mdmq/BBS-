# Generated by Django 2.1.4 on 2019-09-11 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_auto_20190909_1728'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='view_times',
            new_name='read_num',
        ),
    ]