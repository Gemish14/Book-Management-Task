# Generated by Django 4.2.7 on 2024-01-03 08:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0006_alter_book_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="image",
            field=models.ImageField(
                default="static/uploadedImages/default.jpg", upload_to="uploadedImages"
            ),
        ),
    ]
