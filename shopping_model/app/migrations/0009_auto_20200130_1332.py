# Generated by Django 2.2 on 2020-01-30 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20200130_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproducts',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
