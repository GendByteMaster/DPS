from django.urls import path
from .views import CarListView, CarDetailView, AddCarView, SearchCarView, IndexView

# URL-шаблоны для приложения showroom.
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('cars/', CarListView.as_view(), name='car_list'),
    path('cars/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('add_car/', AddCarView.as_view(), name='add_car'),
    path('search_car/', SearchCarView.as_view(), name='search_car'),
]

"""
URL-шаблоны для приложения showroom.

Этот модуль определяет URL-шаблоны для приложения showroom. Включает следующие шаблоны:
- Корневой URL-шаблон ('') отображает главную страницу с помощью IndexView.
- URL-шаблон 'cars/' отображает список всех автомобилей с помощью CarListView.
- URL-шаблон 'cars/<int:pk>/' отображает подробную информацию об автомобиле с помощью CarDetailView.
- URL-шаблон 'add_car/' позволяет добавить новый автомобиль в базу данных с помощью AddCarView.
- URL-шаблон 'search_car/' позволяет искать автомобили по модели с помощью SearchCarView.

Каждый URL-шаблон связан с конкретным классом представления и имеет уникальное имя, которое можно использовать для обратного разрешения URL.

Пример использования:
    Чтобы получить URL-адрес для шаблона 'car_list', можно использовать следующий код:
    ```
    from django.urls import reverse

    url = reverse('car_list')
    ```

Примечание: Этот модуль должен быть включен в основной файл конфигурации URL проекта.
"""
