from django.urls import path
from . import views


app_name = 'cars'


#domain.com/cars/
urlpatterns = [
    
    path('list/', views.all_cars, name='list'), #domain.com/cars/list
    path('delete/', views.delete_cars, name='delete'), #domain.com/cars/delete
    path('add/', views.add_cars, name='add') #domain.com/cars/add

]
