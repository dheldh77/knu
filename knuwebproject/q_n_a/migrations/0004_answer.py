# Generated by Django 2.1.7 on 2019-02-18 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('q_n_a', '0003_auto_20190217_1624'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('body', models.TextField()),
                ('qna', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='q_n_a.QNA')),
            ],
        ),
    ]
