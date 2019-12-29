# Generated by Django 2.2.7 on 2019-12-29 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoardModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('auther', models.CharField(max_length=100)),
                ('images', models.ImageField(upload_to='')),
                ('good', models.IntegerField()),
                ('read', models.IntegerField()),
                ('readtext', models.CharField(max_length=200)),
            ],
        ),
    ]