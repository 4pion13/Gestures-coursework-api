# Generated by Django 5.1.1 on 2024-09-23 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_guitars_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guitars',
            name='price',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
