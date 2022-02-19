from django.contrib import admin
from contactenquiry.models import contactEnquiry

class ContactEnquiry(admin.ModelAdmin):
    list_display=('name','email','phone','websiteLink','message')


admin.site.register(contactEnquiry,ContactEnquiry)

# Register your models here.
