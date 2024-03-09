from django.contrib import admin

from cars.models import Cars


class CarAdmin(admin.ModelAdmin):
    # fields = ['year', 'brand']

    fieldsets = [
        # ('TIME INFORMATION', {'fields': ['year']}),
        # ('CAR INFORMATION', {'fields': ['brand']})

        ('CAR AND TIME', {'fields':['brand', 'year']})
    ]
    pass

# Register your models here.

admin.site.register(Cars, CarAdmin)