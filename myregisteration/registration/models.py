from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):
    fname=models.CharField(max_length=255)
    lname=models.CharField(max_length=255)
    phone=models.IntegerField(null=True)
    joined_date=models.DateField(null=True)

    def __str__(self):
        return f"{self.fname} {self.lname} "
# Create your models here.
