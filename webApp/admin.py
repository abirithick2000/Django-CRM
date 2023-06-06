from django.contrib import admin
from webApp.models import Record

# Register your models here.
class newRecord(admin.ModelAdmin):
    my_list=['created_at','first_name','last_name','email','phone','address','city','state','pincode']
admin.site.register(Record,newRecord)