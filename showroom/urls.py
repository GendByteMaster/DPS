from django.urls import path
from .views import CarListView, CarDetailView, AddCarView, SearchCarView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('cars/', CarListView.as_view(), name='car_list'),
    path('cars/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('add_car/', AddCarView.as_view(), name='add_car'),
    path('search_car/', SearchCarView.as_view(), name='search_car'),
]
