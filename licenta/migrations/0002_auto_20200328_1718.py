# Generated by Django 3.0.4 on 2020-03-28 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('licenta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meals',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='meals',
            name='preparation_time',
            field=models.IntegerField(),
        ),
    ]
