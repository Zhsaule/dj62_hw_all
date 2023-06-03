from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv

CONTENT = list()
list_column = ['Name', 'Street', 'District']
with open('data-398-2018-08-30.csv', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    for dict_item in reader:
        CONTENT.append({key: dict_item[key] for key in dict_item if key in list_column})


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(CONTENT, 10)
    bus_stations = paginator.get_page(page_number)

    context = {
        'bus_stations': bus_stations
    }
    return render(request, 'stations/index.html', context)
