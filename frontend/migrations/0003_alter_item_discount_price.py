# Generated by Django 4.1.3 on 2023-09-08 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("frontend", "0002_alter_item_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="discount_price",
            field=models.FloatField(blank=True, null=True),
        ),
    ]