# Generated by Django 3.0 on 2020-01-21 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0003_friends_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='_from',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='_from', to='practice.Friends'),
        ),
        migrations.AlterField(
            model_name='message',
            name='_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='_to', to='practice.Friends'),
        ),
    ]
