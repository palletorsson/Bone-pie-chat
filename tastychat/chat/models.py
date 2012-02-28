from django.db import models

class Chat(models.Model): # Tweet
    message = models.CharField(max_length=140)
    user = models.CharField(max_length=64, verbose_name="Nick name") # added 
    timestamp = models.DateTimeField(auto_now_add=True)
