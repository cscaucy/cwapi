# Generated by Django 3.0.3 on 2020-03-18 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20200318_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='rank',
            name='teacherid',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
