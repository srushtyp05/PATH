# Generated by Django 5.0.3 on 2024-03-22 22:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("car_ride", "0004_notification"),
    ]

    operations = [
        migrations.AddField(
            model_name="booking",
            name="price",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]