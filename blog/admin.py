from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import *


class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'text']
    list_display = ['title', 'slug','category' ,'created_at','status']
    list_filter = ['category', 'created_at','status']
    prepopulated_fields = {'slug':('title',)}
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title','slug']
    prepopulated_fields = {'slug':('title',)}
# Register your models here.
admin.site.register(Post, PostAdmin,SimpleHistoryAdmin)
admin.site.register(Category, CategoryAdmin)
