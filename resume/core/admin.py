from django.contrib import admin
from core.models import Contact

# Register your models here.
@admin.register(Contact)
class ContactRegister(admin.ModelAdmin):
    list_display=['id','name','email','mob_no','msg']