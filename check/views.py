# from check.models import Result
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import math
from numpy import result_type
import pandas as pd
import pickle
from .forms import *
from .models import *
from django.views.generic import ListView

with open(r'personality_check\Model\personality_model.pkl', 'rb') as f:
    model = pickle.load(f)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('user-login')
    else:
        form = RegisterForm()
    return render(request, 'check/register.html', {'form': form})

def question(request):
    form = PersonalityForm()
    if request.method == 'POST':
        form = PersonalityForm(request.POST)
        user = request.user.id
        if form.is_valid():
            temp={}
            temp['openness']=float(form.cleaned_data.get('Openness'))  
            temp['neuroticism']=float(form.cleaned_data.get('Neuroticism'))
            temp['conscientiousness']=float(form.cleaned_data.get('Conscientiousness'))
            temp['agreeableness']=float(form.cleaned_data.get('Agreeableness'))
            temp['extraversion']=float(form.cleaned_data.get('Extraversion'))      
            testdata=pd.DataFrame({'x':temp}).transpose()
            res=model.predict(testdata)[0]
            prediction = Form(Openness =temp['openness'],Neuroticism=temp['neuroticism'], Conscientiousness=temp['conscientiousness'], Agreeableness=temp['agreeableness'], Extraversion=temp['extraversion'], Result = res,User_id = user)
            prediction.save()

            return render(request,'check/result.html',{'result':res})
        
        
    context = {'form':form}
    return render(request,'check/personality_form.html',context)

@login_required
def profile(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST,instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('user-profile')

    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'p_form': p_form
    }

    return render(request, 'check/profile.html', context)

@login_required
def UserRes(request):
    res = Form.objects.filter(User = request.user.id)
    res = res.order_by('-Date')
    context = {
        'results' : res
        }

    return render(request,'check/test.html',context)

def about(request):
    return render(request, 'check/about.html', {'title': 'About'})

@login_required
def description(request):
    return render(request, 'check/description.html', {'title': 'desc'})