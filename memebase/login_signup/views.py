# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django import forms
from django.http import HttpResponseRedirect
from .forms import UserRegistrationForm
import re


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email = userObj['email']
            password = userObj['password']
            if isValidEmail(email):
                if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                    User.objects.create_user(username, email, password)
                    user = authenticate(username=username, password=password)
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponse('Looks like a username with that email or password already exists', status=400)
            else:
                return HttpResponse('Email id is Invalid', status=400)

    else:
        form = UserRegistrationForm()
    return render(request, 'login_signup/register.html', {'form': form})


def isValidEmail(email):
    if len(email) > 7:
        if re.match("[^@]+@[^@]+\.[^@]+", email) is not None:
            return True

        return False