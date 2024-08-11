from django.contrib import admin

from .models import (
    NewsModel, CategoryModel, ContactModel, CommentModel
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
    prepopulated_fields = {'slug':('name',)}
    

@admin.register(ContactModel)

class ContactModelAdmin(admin.ModelAdmin):
    search_fields = ['name',]
    list_display = ['name', 'email']
    list_filter = ['name', 'email']


@admin.register(CommentModel)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'body', 'created_time', 'active']
    list_filter = ['active', 'created_time']
    search_fields = ['user', 'body']
    actions = ['disable_comments', 'activate_comments']

    def disable_comments(self, request, queryset):
        queryset.update(active=False)

    def activate_comments(self, request, queryset):
        queryset.update(active=True)


