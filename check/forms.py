from django import forms
from django.db.models import fields
from django.forms.models import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Form, Profile

CHOICES = [(1,"1"),(2,"2"),(3,"3"),(4,"4"),(5,"5"),(6,"6"),(7,"7"),(8,"8")]

class PersonalityForm(ModelForm):
    class Meta:
        model = Form
        fields = ['Openness','Neuroticism', 'Conscientiousness', 'Agreeableness', 'Extraversion' ]

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','password1','password2']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['Name',"Age","Gender"]