# Generated by Django 3.0.4 on 2020-03-29 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('licenta', '0004_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='meals',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='licenta.Category'),
        ),
    ]