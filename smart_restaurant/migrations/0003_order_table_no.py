# Generated by Django 4.0 on 2022-11-09 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smart_restaurant', '0002_remove_order_items_order_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='table_no',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
