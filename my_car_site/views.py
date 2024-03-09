from django.shortcuts import render

def home(request):

    return render(request, 'base.html')


def cars(request):

    return render(request, 'cars.html')