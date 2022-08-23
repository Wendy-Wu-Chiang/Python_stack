from django.db import models

class CoursesManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 6:
            errors["name"] = "Course name should be more than 5 characters"
        if len(postData['description']) < 16:
            errors["description"] = "Course description should be more than 15 characters."
        return errors

class Courses(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CoursesManager()         
