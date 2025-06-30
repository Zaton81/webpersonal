from django.contrib import admin
from .models import Books
# Register your models here.
class BooksAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
admin.site.register(Books, BooksAdmin)
# Register your models here.
