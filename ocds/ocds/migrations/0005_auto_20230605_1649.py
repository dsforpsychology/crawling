# Generated by Django 3.1.3 on 2023-06-05 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocds', '0004_auto_20230605_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventinfo',
            name='stateNo',
            field=models.IntegerField(default=0),
        ),
    ]