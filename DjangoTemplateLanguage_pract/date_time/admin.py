from django.contrib import admin
from .models import Date_filter, Day, Week, Month, Year, TimeFilter, Predefined_format

admin.site.register((Date_filter, Day, Week, Month, Year))
admin.site.register(TimeFilter)
admin.site.register(Predefined_format)