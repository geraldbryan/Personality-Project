# Generated by Django 3.2.4 on 2021-09-08 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0007_rename_form_predict_form_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='Result',
            field=models.TextField(default='DEFAULT VALUE', max_length=128),
        ),
        migrations.DeleteModel(
            name='predict',
        ),
    ]
