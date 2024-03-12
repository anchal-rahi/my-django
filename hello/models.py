from django.db import models

# Create your models here.

class contact(models.Model):
    username=models.CharField(max_length=200)
    useremail=models.CharField( max_length=250)
    phonenumber=models.IntegerField()
    message=models.TextField()
    myimage = models.ImageField(upload_to = "usermedia", null = True, blank = True)
