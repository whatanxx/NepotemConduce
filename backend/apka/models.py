from django.db import models

#placeholder bo nie wiem jak dodac np imagesy jako rodzaj pola zeby zrobic calosc
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    desc = models.CharField(max_length=255)

