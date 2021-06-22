from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors={}
        email_checker = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['pw']) < 8:
            errors['pw'] = "Your password must be at least 8 characters long."
        if len(postData['fname']) < 2 or len(postData['lname']) < 2:
            errors['name'] = "Your name must be at least 2 characters long."
        if not email_checker.match(postData['email']):
            errors['email'] = 'Must enter a valid email.'
        if postData['pw'] != postData['confpw']:
            errors['pw'] = 'Password and Confirm Password must match.'
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    objects = UserManager()

class Wall_Message(models.Model):
    message = models.TextField(max_length=255)
    poster = models.ForeignKey(User, related_name='user_messages', on_delete=models.CASCADE)
    user_likes = models.ManyToManyField(User, related_name='liked_posts')

class Comment(models.Model):
    comment = models.CharField(max_length=255)
    poster = models.ForeignKey(User, related_name='user_comments', on_delete=models.CASCADE)
    wall_message = models.ForeignKey(Wall_Message, related_name="post_comments", on_delete=models.CASCADE)