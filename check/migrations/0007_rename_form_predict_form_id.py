# Generated by Django 3.2.4 on 2021-09-08 04:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0006_alter_form_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='predict',
            old_name='form',
            new_name='form_id',
        ),
    ]
