# Generated by Django 3.2.4 on 2021-09-08 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0004_predict_form'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
