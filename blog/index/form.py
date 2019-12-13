from django.forms import Form,fields,widgets
from django import forms

class Resgister_form(Form):
    user_name=fields.CharField(min_length=6,max_length=20)
    password=fields.CharField(min_length=6,max_length=15,widget=forms.PasswordInput)
    password_repeat=fields.CharField(min_length=6,max_length=15,widget=forms.PasswordInput)

class Login_form(Form):
    user_name=fields.CharField(min_length=6,max_length=20)
    password=fields.CharField(min_length=6,max_length=15,widget=forms.PasswordInput)



