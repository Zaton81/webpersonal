from django.contrib import admin
from .models import Pages

# Register your models here.
class PagesAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Pages, PagesAdmin)