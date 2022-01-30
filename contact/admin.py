from django.contrib import admin
from .models import Contacts
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'email', 'time')
    search_fields = ('email', )

admin.site.register(Contacts,ContactAdmin)
