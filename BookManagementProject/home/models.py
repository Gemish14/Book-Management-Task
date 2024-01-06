from django.db import models
from django.contrib.auth.models import User

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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField("Enter Full Name", max_length=50)
    stud_id = models.IntegerField("Enter Roll No.",primary_key=True)
    email = models.EmailField("Enter Email",null=True)
    password = models.CharField("Enter Password", max_length=20,null=False,default = 'VJTI@Student') 
    
    def __str__(self):
        return self.name

    class Meta : 
        db_table = 'student' 

class Transaction(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} reserved {self.book.title}"

    