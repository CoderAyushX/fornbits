from django.contrib import admin
from .models import Category,Post,blogpostComment
# Register your models here.
#admin customizing
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'timestamp')
    search_fields = ('title', )

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'upload_time')
    search_fields = ('title', )
    list_filter = ('cat',)
    list_per_page = 50

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'timestamp')
    search_fields = ('user', )
    list_filter = ('post',)
    list_per_page = 50

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(blogpostComment, CommentAdmin)