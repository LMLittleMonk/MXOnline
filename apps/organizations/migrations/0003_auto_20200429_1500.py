# Generated by Django 2.2 on 2020-04-29 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0002_auto_20200429_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='tea_workyears',
            field=models.IntegerField(verbose_name='工作年限'),
        ),
    ]