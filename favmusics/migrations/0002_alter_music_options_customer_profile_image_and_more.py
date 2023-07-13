# Generated by Django 4.2.3 on 2023-07-13 16:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("favmusics", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="music",
            options={"verbose_name": "Musician"},
        ),
        migrations.AddField(
            model_name="customer",
            name="profile_image",
            field=models.ImageField(null=True, upload_to="images/"),
        ),
        migrations.AlterField(
            model_name="customer",
            name="dob",
            field=models.DateField(null=True, verbose_name="Date Of Birth"),
        ),
    ]