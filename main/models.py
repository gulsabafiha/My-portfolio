from django.db import models

# Create your models here.
class ContactModel(models.Model):
    name= models.CharField(max_length=150)
    email= models.EmailField()
    message= models.CharField(max_length=500)