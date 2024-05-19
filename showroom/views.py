from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from .models import Car, Brand, Stock

# Класс для отображения главной страницы
class IndexView(View):
    """
    Представление для отображения главной страницы.
    """
    def get(self, request):
        return render(request, 'showroom/index.html')

# Класс для отображения списка автомобилей
class CarListView(View):
    """
    Представление для отображения списка всех автомобилей.
    """
    def get(self, request):
        cars = Car.objects.all()
        return render(request, 'showroom/car_list.html', {'cars': cars})

# Класс для отображения детальной информации об автомобиле
class CarDetailView(View):
    """
    Представление для отображения подробной информации об автомобиле.
    """
    def get(self, request, pk):
        car = get_object_or_404(Car, pk=pk)
        return render(request, 'showroom/car_detail.html', {'car': car})

# Класс для добавления автомобиля в базу данных
class AddCarView(View):
    """
    Представление для добавления нового автомобиля в базу данных.
    """
    def post(self, request):
        # Получаем бренд по имени, указанному в POST-запросе
        brand = get_object_or_404(Brand, name=request.POST['brand'])
        
        # Создаем новый объект автомобиля
        car = Car.objects.create(
            model=request.POST['model'],
            engine_capacity=request.POST['engine_capacity'],
            doors=request.POST['doors'],
            color=request.POST['color'],
            price=request.POST['price'],
            year=request.POST['year'],
            brand=brand
        )
        
        # Создаем запись на складе для нового автомобиля
        Stock.objects.create(car=car)
        
        return HttpResponse("Автомобиль успешно добавлен")

# Класс для поиска автомобиля по модели
class SearchCarView(View):
    """
    Представление для поиска автомобилей по модели.
    """
    def get(self, request):
        # Получаем модель из GET-запроса
        model_name = request.GET.get('model', '')
        
        # Фильтруем автомобили по частичному совпадению модели
        cars = Car.objects.filter(model__icontains=model_name)
        
        return render(request, 'showroom/car_list.html', {'cars': cars})
