# Generated by Django 4.0 on 2022-11-13 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smart_restaurant', '0005_rename_item_type_item_is_non_veg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='item_category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='item_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='item_price',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='item',
            name='item_serial_no',
        ),
        migrations.AddField(
            model_name='item',
            name='rank',
            field=models.PositiveIntegerField(default=0),
        ),
    ]