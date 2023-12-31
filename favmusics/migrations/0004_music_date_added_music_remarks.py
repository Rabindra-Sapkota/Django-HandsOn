# Generated by Django 4.2.3 on 2023-07-17 18:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("favmusics", "0003_alter_customer_profile_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="music",
            name="date_added",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="music",
            name="remarks",
            field=models.TextField(default="no remark"),
            preserve_default=False,
        ),
    ]
