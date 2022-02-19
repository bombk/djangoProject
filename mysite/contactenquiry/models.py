from email import message
from django.db import models
##create model 
class contactEnquiry(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    websiteLink=models.CharField(max_length=70)
    message=models.TextField()

# Create your models here.
