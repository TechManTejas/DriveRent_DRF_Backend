from django.contrib import admin
from .models import Car

class CarAdmin(admin.ModelAdmin):
    list_display = ('company', 'model', 'number') 
    list_filter = ('company', 'model') 
    search_fields = ('company', 'model', 'number') 

admin.site.register(Car, CarAdmin)
