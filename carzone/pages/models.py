from django.db import models

# Create your models here.


class Team(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    facebook_link = models.URLField(max_length=200)
    google_plus_link = models.URLField(max_length=100)
    twitter_link = models.URLField(max_length=100, default="")
    created_date = models.DateTimeField(auto_now_add=True)
    photo: models.ImageField(upload_to='photos/%Y/%m/%d')

    def __str__(self):
        return self.first_name
