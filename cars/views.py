from django.shortcuts import render, redirect
from django.urls import reverse
from . import models

# Create your views here.


def all_cars(request):
    all_cars = models.Cars.objects.all()

    context = {'all_cars':all_cars}

    return render(request, 'cars/list.html', context=context)


def add_cars(request):
    if request.POST:
        brand = request.POST['brand']
        year = int(request.POST['year'])

        models.Cars.objects.create(brand=brand, year=year)


    #if user submits new car got to --> LIST.html

        return redirect(reverse('cars:list'))
    
    else: 
        return render(request, 'cars/add.html')


def delete_cars(request):
    if request.POST:
        pk = request.POST['pk']

        try:
            models.Cars.objects.get(pk=pk).delete()
            return redirect(reverse('cars:list'))

        except:
            print("Pk not found")
            return redirect(reverse('cars:list'))

    else:
        return render(request, 'cars/delete.html')

    