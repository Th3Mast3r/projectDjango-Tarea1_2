from django.contrib import admin
from . models import (
    Blog,
    Contact,
    Media,
    Review,
)

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'timestamp', 'name')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_active')
    readonly_fields = ('slug',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_active')
    readonly_fields = ('slug',)


#aqui se maneja la parte administrativa y se puede visualizar la base de datos por medio del localhost
#y para ver todas las tablas

