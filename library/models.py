from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/covers', blank=True, null=True)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=20, unique=True)
    publisher = models.CharField(max_length=255)
    publication_date = models.DateField()
    pages = models.PositiveIntegerField()
    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Course(models.Model):
    title = models.CharField(max_length=300)
    price = models.IntegerField()

class  Group(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    student_count = models.IntegerField()

    def __str__(self):
        return self.title