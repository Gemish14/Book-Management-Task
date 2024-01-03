# Generated by Django 4.2.7 on 2024-01-03 08:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0003_book_category_student_email_alter_student_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="category",
            field=models.CharField(default="Unknown Category", max_length=10),
        ),
        migrations.AlterField(
            model_name="book",
            name="image",
            field=models.ImageField(
                default="static/uploadedImages/default.jpg",
                upload_to="BookManagementProject/home/static/uploadedImages",
            ),
        ),
    ]
