from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    logo = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    editor = models.CharField(max_length=50)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=50)
    isbn = models.CharField(max_length=100)

    def __str__(self):
     return str(self.title)

class Summary(models.Model):
    book = models.ForeignKey(Book,on_delete = models.CASCADE)
    summary = models.TextField(max_length=600)

    def __str__(self):
     return str(self.summary)
