from django.shortcuts import render
from .models import Date_filter, Day, Week, TimeFilter, Month, Year, Predefined_format

def index_(request):

    context = {}
    return render(request, 'date_time/index.html', context)

def date_time(request):

    date_filter = Date_filter.objects.all().order_by('-id')
    days = Day.objects.all().order_by('-id')
    week = Week.objects.get(id=1)
    months = Month.objects.all().order_by('-id')
    years = Year.objects.all().order_by('-id')
    time_filters = TimeFilter.objects.all()
    predefined_formats = Predefined_format.objects.all()

    context = {'date_filters': date_filter, 'days': days, 'week': week, 'months': months, 'years': years, 'time_filters': time_filters, 'predefined_formats': predefined_formats}
    return render(request, 'date_time/date_time.html', context)