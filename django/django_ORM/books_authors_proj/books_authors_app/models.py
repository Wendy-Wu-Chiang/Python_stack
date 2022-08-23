from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Authors(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    note = models.TextField()
    myBooks = models.ManyToManyField(Book, related_name='myAuthors')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
