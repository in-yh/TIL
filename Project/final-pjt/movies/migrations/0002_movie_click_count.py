# Generated by Django 3.2.13 on 2022-11-20 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='click_count',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]