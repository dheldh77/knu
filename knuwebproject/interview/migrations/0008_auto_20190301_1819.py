# Generated by Django 2.1.7 on 2019-03-01 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0007_auto_20190301_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pic',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]