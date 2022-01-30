from django.contrib import admin
from .models import Rate,Feedback,whatsnew
# # Register your models here.

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('sender', 'timestamp')
    search_fields = ('sender', )

admin.site.register(Rate)
admin.site.register(whatsnew)
admin.site.register(Feedback, FeedbackAdmin)
