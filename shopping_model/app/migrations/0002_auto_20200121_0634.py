# Generated by Django 2.2 on 2020-01-21 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.CharField(max_length=300),
        ),
    ]
