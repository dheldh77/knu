# Generated by Django 2.1.5 on 2019-03-01 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('q_n_a', '0006_auto_20190222_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]