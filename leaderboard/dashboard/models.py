from django.db import models

def Details(models.Model):
    full_name = models.CharField(max_length = 160)
    user_name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 100)
    total_points = models.IntegerField()
