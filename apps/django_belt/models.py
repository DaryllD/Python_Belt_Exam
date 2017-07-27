from __future__ import unicode_literals
from django.db import models
from django import forms
import bcrypt


class UserManager(models.Manager):
    def validateRegistration(self, form_data):
        print "Inside UserManager"
        print len(form_data['f_l_name'])
        errors = []

        if len(form_data['f_l_name']) < 3:
            errors.append("Valid Name is Required")
        if len(form_data['user_name']) < 3:
            errors.append("Valid User Name is Required")
        if len(form_data['password']) < 8:
            errors.append("Valid Password is Required")
        if form_data['password'] != form_data['password_confirmation']:
            errors.append("Passwords do not match.")

        return errors

    def createUser(self, form_data):
        password = str(form_data['password'])
        hashed_pw = bcrypt.hashpw(password, bcrypt.gensalt())
        user = User.objects.create(
            f_l_name = form_data['f_l_name'],
            user_name = form_data['user_name'],
            password = hashed_pw,
        )

        return user

    def validate_login(self, form_data):
        print "inside Validate"
        print len(form_data)

        errors = []

        if len(form_data['user_name']) < 3:
            errors.append("Valid User Name is Required.")
        if len(form_data['password']) < 8:
            errors.append("Valid Password is required")

        return errors


class User(models.Model):
    f_l_name = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    objects = UserManager()

class Item(models.Model):
    item_name = models.CharField(max_length=255)
    added_by = models.ForeignKey(User, related_name='users_add')
    selected_by = models.ForeignKey(User, related_name='users_select')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
