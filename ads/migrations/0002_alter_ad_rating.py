# Generated by Django 5.1.4 on 2024-12-15 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='rating',
            field=models.DecimalField(decimal_places=1, max_digits=1),
        ),
    ]
