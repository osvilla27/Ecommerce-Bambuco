# Generated by Django 3.2.20 on 2023-08-12 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20230812_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variants',
            name='image_id',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
