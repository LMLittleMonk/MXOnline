# Generated by Django 2.2 on 2020-05-14 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': '教师', 'verbose_name_plural': '教师'},
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='tea_click',
            new_name='click_nums',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='tea_collect',
            new_name='fav_nums',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='tea_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='tea_org',
            new_name='org',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='tea_age',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='tea_company',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='tea_features',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='tea_name',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='tea_position',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='tea_workyears',
        ),
        migrations.AddField(
            model_name='teacher',
            name='age',
            field=models.IntegerField(default=18, verbose_name='年龄'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='name',
            field=models.CharField(default='', max_length=50, verbose_name='教师名'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='points',
            field=models.CharField(default='好', max_length=50, verbose_name='教学特点'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='work_company',
            field=models.CharField(default='', max_length=50, verbose_name='就职公司'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='work_position',
            field=models.CharField(default='', max_length=50, verbose_name='公司职位'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='work_years',
            field=models.IntegerField(default=0, verbose_name='工作年限'),
        ),
    ]