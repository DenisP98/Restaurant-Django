# Generated by Django 3.0.4 on 2020-03-30 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('licenta', '0005_meals_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]