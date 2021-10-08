from django.contrib import admin
from .models import *


# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'create_at', 'is_published', 'category')
    search_fields = ('title', 'content')
    list_filter = ('is_published', 'category')
    list_display_links = ('title',)
    save_on_top = True


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('title',)
    list_display_links = ('title',)
    save_on_top = True


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
