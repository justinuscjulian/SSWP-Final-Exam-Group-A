# Generated by Django 3.1.2 on 2020-11-01 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_list', '0002_auto_20201101_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='s_address',
            field=models.CharField(max_length=50, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='student',
            name='s_class',
            field=models.CharField(max_length=10, verbose_name='Class'),
        ),
        migrations.AlterField(
            model_name='student',
            name='s_dob',
            field=models.DateField(null=True, verbose_name='Date of Birth'),
        ),
        migrations.AlterField(
            model_name='student',
            name='s_email',
            field=models.CharField(max_length=30, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='student',
            name='s_name',
            field=models.CharField(max_length=30, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='student',
            name='s_phonenum',
            field=models.CharField(max_length=20, verbose_name='Phone Number:'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='t_address',
            field=models.CharField(max_length=50, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='t_dob',
            field=models.DateField(null=True, verbose_name='Date of Birth'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='t_email',
            field=models.CharField(max_length=30, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='t_name',
            field=models.CharField(max_length=30, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='t_phonenum',
            field=models.CharField(max_length=20, verbose_name='Phone Number:'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='t_subject',
            field=models.CharField(max_length=30, verbose_name='Subject'),
        ),
    ]
