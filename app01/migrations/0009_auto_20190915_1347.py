# Generated by Django 2.1.4 on 2019-09-15 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0008_auto_20190911_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app01.Column'),
        ),
    ]
