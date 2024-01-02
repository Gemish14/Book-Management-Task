from django.db import models
import secrets

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    pagesCount = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='static/uploadedImages/',default='static/uploadedImages/default.jpeg')

    def __str__(self):
        return self.title 
    
class Student(models.Model):
    name = models.CharField(max_length=50)
    stud_id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.name 