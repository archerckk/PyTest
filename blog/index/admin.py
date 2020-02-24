from django.contrib import admin
from .models import Question,Article,Comment

# Register your models here.
admin.site.register(Question)
admin.site.register(Article)
admin.site.register(Comment)