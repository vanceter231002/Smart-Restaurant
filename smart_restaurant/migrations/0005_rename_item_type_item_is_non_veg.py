# Generated by Django 4.0 on 2022-11-13 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smart_restaurant', '0004_item_item_category_item_item_serial_no_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='item_type',
            new_name='is_non_veg',
        ),
    ]
