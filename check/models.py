from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=CASCADE)
    Name = models.CharField(max_length=250, null=True)
    Gender = models.CharField(max_length=20, null= True)
    Age = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

CHOICES = [(1,"1"),(2,"2"),(3,"3"),(4,"4"),(5,"5"),(6,"6"),(7,"7"),(8,"8")]

class Form(models.Model):
    Openness = models.PositiveSmallIntegerField(choices=CHOICES, default=4)
    Neuroticism = models.PositiveSmallIntegerField(choices=CHOICES, default=4)
    Conscientiousness = models.PositiveSmallIntegerField(choices=CHOICES, default=4)
    Agreeableness = models.PositiveSmallIntegerField(choices=CHOICES, default=4)
    Extraversion = models.PositiveSmallIntegerField(choices=CHOICES, default=4)
    Result = models.TextField(max_length=128,default='DEFAULT VALUE')
    User = models.ForeignKey(User, on_delete=CASCADE,null=True)
    Date = models.DateField(auto_now=True)