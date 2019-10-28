# Generated by Django 2.2.4 on 2019-10-22 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectMain', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinic',
            name='address',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='clinic',
            name='cancelled',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='clinic',
            name='finished',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='clinic',
            name='skipped',
            field=models.IntegerField(default=0),
        ),
    ]