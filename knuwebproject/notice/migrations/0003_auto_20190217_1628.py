# Generated by Django 2.1.7 on 2019-02-17 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0002_pic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notice',
            options={'ordering': ('id',)},
        ),
    ]