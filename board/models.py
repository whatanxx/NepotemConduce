from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.

class Experience(models.Model):
    experience = models.CharField(max_length=100)
    def __str__(self):
        return self.experience
    

class Gender(models.Model):
    gender = models.CharField(max_length=50)
    def __str__(self):
        return self.gender
    
class City(models.Model):
    city_name = models.CharField(max_length=100)
    def __str__(self):
        return self.city_name
    
class Duty(models.Model):
    duty = models.CharField(max_length=100)
    def __str__(self):
        return self.duty
    
from django.db import models
from django.contrib.auth.models import User

class Volunteer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(90)])
    phone_number = models.CharField(max_length=15)
    gender = models.ForeignKey(Gender, null=True, on_delete=models.SET_NULL)
    experience = models.ForeignKey(Experience, null=True, on_delete=models.SET_NULL)
    duties = models.ManyToManyField(Duty)
    city = models.ForeignKey(City, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Independence(models.Model):
    independence = models.CharField(max_length=150)
    def __str__(self):
        return self.independence

class Senior(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(90)])
    phone_number = models.CharField(max_length=15)
    gender = models.ForeignKey(Gender, null=True, on_delete=models.SET_NULL)
    independence = models.ForeignKey(Independence, null=True, on_delete=models.SET_NULL)
    duties = models.ManyToManyField(Duty)
    city = models.ForeignKey(City, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
