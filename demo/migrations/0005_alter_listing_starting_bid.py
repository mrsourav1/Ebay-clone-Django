# Generated by Django 4.0.6 on 2022-07-22 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0004_alter_listing_current_bid_alter_listing_starting_bid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='starting_bid',
            field=models.IntegerField(),
        ),
    ]
