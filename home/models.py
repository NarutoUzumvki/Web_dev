from django.db import models

# Create your models here.

class Form(models.Model):

    name=models.CharField(max_length=128)
    email=models.CharField(max_length=128)
    password=models.CharField(max_length=20)
    desc= desc=models.TextField()
    date=models.DateField()


    def __str__(self):
        return self.name + "  -  " + self.email
    



