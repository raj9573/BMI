from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class BMI(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    age=models.IntegerField()
    height=models.DecimalField(max_digits=5,decimal_places=2)
    weight=models.DecimalField(max_digits=5,decimal_places=2)
    mobile_number=models.CharField(max_length=10)
    BMI=models.DecimalField(max_digits=5,decimal_places=2)

