# Generated by Django 2.2.5 on 2019-09-29 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_app', '0002_auto_20190929_1020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
