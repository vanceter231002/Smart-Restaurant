# Generated by Django 4.0 on 2022-11-13 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smart_restaurant', '0008_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='contains_egg',
            field=models.BooleanField(default=False),
        ),
    ]
