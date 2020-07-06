from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'author', 'year')
    search_fields = ['title', 'description']
	
admin.site.register(Book, BookAdmin)


