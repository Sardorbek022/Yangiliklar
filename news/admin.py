from django.contrib import admin

from .models import (
    NewsModel, CategoryModel, ContactModel
)


# admin.site.register([NewsModel, CategoryModel, ContactModel])
@admin.register(NewsModel)

class NewsModelAdmin(admin.ModelAdmin):
    search_fields = ['title',]
    list_display = ['title', 'slug', 'publish_time', 'image']
    list_filter = ['title', ]
    prepopulated_fields = {'slug':('title',)}
    
      
@admin.register(CategoryModel)

class CategoryModelAdmin(admin.ModelAdmin):
    search_fields = ['name',]
    list_display = ['name',]
    list_filter = ['name', ]
    

@admin.register(ContactModel)

class ContactModelAdmin(admin.ModelAdmin):
    search_fields = ['name',]
    list_display = ['name', 'email']
    list_filter = ['name', 'email']