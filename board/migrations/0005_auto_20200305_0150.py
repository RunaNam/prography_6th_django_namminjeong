# Generated by Django 2.2.10 on 2020-03-04 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_auto_20200305_0017'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='owner',
            new_name='user',
        ),
    ]
