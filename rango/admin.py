from django.contrib import admin
from .models import Page
from rango.models import Category, Page
from rango.models import UserProfile
from .models import UserProfile
from django.contrib import admin

class PageAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'url','views')  # 按顺序显示这三个字段

admin.site.register(Page, PageAdmin)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    
admin.site.register(Category, CategoryAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    pass
