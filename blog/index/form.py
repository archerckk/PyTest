from django.forms import Form,fields,widgets
from django import forms

class Resgister_form(Form):
    user_name=fields.CharField(min_length=6,max_length=20,error_messages={'required':'请输入你的用户名！',
                                                                          'min_length':'用户名的长度小于6',
                                                                          })
    password=fields.CharField(min_length=6,max_length=15,widget=forms.PasswordInput,error_messages={'required':'请输入你的密码！',
                                                                          'min_length':'密码的长度小于6',
                                                                          })
    password_repeat=fields.CharField(min_length=6,max_length=15,widget=forms.PasswordInput,error_messages={'required':'请输入确认密码！',
                                                                          'min_length':'确认密码的长度小于6',
                                                                          })

class Login_form(Form):
    user_name=fields.CharField(min_length=6,max_length=20,error_messages={'required':'请输入你的用户名！',
                                                                          'min_length':'用户名的长度小于6',
                                                                          })
    password=fields.CharField(min_length=6,max_length=15,widget=forms.PasswordInput,error_messages={'required':'请输入你的密码！',
                                                                          'min_length':'密码的长度小于6',
                                                                          })



