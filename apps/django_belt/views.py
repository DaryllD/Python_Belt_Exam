from django.shortcuts import render, redirect
from django import forms
from models import *
from django.contrib import messages
import bcrypt


def flashErrors(request, errors):
    print "FlashError"
    for error in errors:
        messages.error(request, error)

def index(request):
    print "inside Main"

    return render(request, 'django_belt/index.html')

def login(request):
    print "inside login"
    if request.method =="POST":
        errors = []
        #User.objects.validate_login(request.POST)

        if not errors:
            user = request.session['user_name']
            if user:
                password = str(request.POST['password'])
                user_password = str(user.password)

                hashed_pw = bcrypt.hashpw(password, user_password)

                if hashed_pw == user.password:
                    request.session['user_id'] = user.id
                    return redirect('/create')

            errors.append("Invalid account information.")

        #print errors
        flashErrors(request, errors)

    return redirect('/')

def register(request):
    print "inside register method"
    if request.method == "POST":
        errors = User.objects.validateRegistration(request.POST)

        if not errors:
            user = User.objects.createUser(request.POST)
            request.session['user_id'] = user.id
            return redirect('/create')

        flashErrors(request, errors)

    return redirect('/')
def wishlist(request):
    print "inside Wishlist"

    return render(request, 'django_belt/index.html')
#
def create(request):
    print "inside Create"

    return render(request, 'django_belt/index.html')
#
def remove(request):
    print "inside Remove"


    return redirect('/wishlist')
def logout(request):
    if 'user_id' in request.session:
        request.session.pop('user_id')


    return redirect('/')
