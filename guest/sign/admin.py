from django.contrib import admin
from sign.models import Event,Guest
# Register your models here.



# admin.site.register(Event)
# admin.site.register(Guest)

class EventAdmin(admin.ModelAdmin):
    list_display = ['id','name','status','address','start_time']
    search_fields = ['name']#搜索栏
    list_filter = ['status']#过滤器
class GuessAdmin(admin.ModelAdmin):
    list_display = ['realname','email','sign','create_time','event']
    search_fields = ['phone','realname']#搜索栏
    list_filter = ['sign'] ##过滤器


admin.site.register(Event,EventAdmin)
admin.site.register(Guest,GuessAdmin)