from django.contrib import admin
from .models import CarModel, Engine, Price

# Register your models here.
class PriceAdmin(admin.ModelAdmin):
    list_display=('id','price')
admin.site.register(CarModel)
admin.site.register(Engine)
admin.site.register(Price,PriceAdmin)