from django.db import models
import re

class UserManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}
        if len(postData['name']) < 2:
            errors["name"] = "Name should be at least 2 characters!"
        if len(postData['alias']) < 2:
            errors["alias"] = "Alias should be at least 2 characters!"

        email_regex = re.compile(
            r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        if len(postData['email']) == 0:
            errors["email"] = "Please enter an email!"
        if not email_regex.match(postData['email']):
            errors["email"] = "Please enter a valid email!"

        current_user=User.objects.filter(email=postData['email'])
        if len(current_user) > 0:
            errors['duplicate']= "That email has already been used!"

        if len(postData['password']) < 8:
            errors['password']= "Password must be at least 8 characters long!"
        if postData['password'] != postData['confirm_password']:
            errors['mismatch']= "Sorry,password does not match, please try agian!"        

        return errors

    def login_validator(self, postData):
        errors = {}
        existing_user = User.objects.filter(email=postData['email'])
        if len(postData['email']) == 0:
            errors["email"] = "Please enter your email!"
        if len(postData['password']) < 8:
            errors['password']= "Password not matching, please try agian!"  
        elif bcrypt.checkpw(postData['password'].encode(), existing_user[0].password.encode()) !=True:
            errors['password']= "Email and password do not match!"

class BookManager(models.Manager):
    def book_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "Title must be at least 2 characters"
        return errors
      
class AuthorManager(models.Manager):
    def author_validator(self, postData):
        errors = {}
        if len(postData['author_name']) < 2:
            errors['author_name'] = "Name must be at least 2 characters"
        author_in_db = Author.objects.filter(name=postData['author_name'])
        if len(author_in_db) >0:
            errors['duplicate'] = "Author already exists."
        return errors

class ReviewManager(models.Manager):
    def review_validator(self, postData):
        errors = {}
        if len(postData['content']) < 10:
            errors['content'] = "Please leave review of at least 10 characters"
        return errors


class User(models.Model):
    name = models.CharField(max_length=45)
    alias= models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()         

class Book(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()

class Author(models.Model):
    name = models.CharField(max_length=75)
    books = models.ManyToManyField(Book, related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AuthorManager()

class Review(models.Model):
    content = models.TextField()
    rating = models.IntegerField()
    user_review = models.ForeignKey(User, related_name="user_reviews", on_delete=models.CASCADE)
    book_reviewed = models.ForeignKey(Book, related_name="book_reviews", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()