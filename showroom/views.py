from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from .models import Car, Brand, Stock

class IndexView(View):
    def get(self, request):
        return render(request, 'showroom/index.html')

class CarListView(View):
    def get(self, request):
        cars = Car.objects.all()
        return render(request, 'showroom/car_list.html', {'cars': cars})

class CarDetailView(View):
    def get(self, request, pk):
        car = get_object_or_404(Car, pk=pk)
        return render(request, 'showroom/car_detail.html', {'car': car})

class AddCarView(View):
    def post(self, request):
        brand = get_object_or_404(Brand, name=request.POST['brand'])
        car = Car.objects.create(
            model=request.POST['model'],
            engine_capacity=request.POST['engine_capacity'],
            doors=request.POST['doors'],
            color=request.POST['color'],
            price=request.POST['price'],
            year=request.POST['year'],
            brand=brand
        )
        Stock.objects.create(car=car)
        return HttpResponse("Автомобиль успешно добавлен")

class SearchCarView(View):
    def get(self, request):
        model_name = request.GET.get('model', '')
        cars = Car.objects.filter(model__icontains=model_name)
        return render(request, 'showroom/car_list.html', {'cars': cars})
