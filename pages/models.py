from django.db import models

# Create your models here.

# model no. 1: Creating model for Team

class Team(models.Model):
    ''' to build team model we required following details /
    firstname, lastname, photo,  designation, facebook_link, twitter_link, google_plus'''

    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    designation = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    facebook_link = models.URLField(max_length=100)
    twitter_link = models.URLField(max_length=100)
    google_plus_link = models.URLField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
