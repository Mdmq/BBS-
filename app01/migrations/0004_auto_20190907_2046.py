# Generated by Django 2.1.4 on 2019-09-07 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20190903_2044'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ['-created_time']},
        ),
        migrations.RemoveField(
            model_name='topic',
            name='author',
        ),
        migrations.AlterField(
            model_name='topic',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app01.Column'),
        ),
    ]
