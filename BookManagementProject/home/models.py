from django.db import models

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    pagesCount = models.IntegerField()
    price = models.IntegerField()
    category = models.CharField(max_length=10, default="Unknown Category")
    image = models.ImageField(upload_to='uploaded_images/',default='static/uploadedImages/default.jpg')

    def __str__(self):
        return self.title 
    
class Student(models.Model):
    name = models.CharField("Enter Full Name", max_length=50)
    stud_id = models.IntegerField("Enter Roll No.",primary_key=True)
    email = models.EmailField("Enter Email",null=True)

    """  def __str__(self):
        return self.name """ 

    class Meta : 
        db_table = 'student' 

    