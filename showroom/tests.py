from django.test import TestCase
from showroom.models import Brand, Car, Accessories, Price, Stock, Order, Revoke

class ShowroomModelTest(TestCase):
    """
    Тестовый класс для проверки моделей приложения Showroom.

    Этот класс тестов включает в себя тесты для следующих моделей:
    - Brand: модель для представления бренда автомобилей.
    - Car: модель для представления автомобиля, связанного с брендом.
    - Accessories: модель для представления аксессуаров, связанных с автомобилями.
    - Price: модель для представления цены автомобиля.
    - Stock: модель для представления складских записей о количестве автомобилей.
    - Order: модель для представления заказов на автомобили.
    - Revoke: модель для представления отмен заказов и причин отмены.

    Для каждой модели проверяются корректность создания и связи между моделями.
    """

    def setUp(self):
        # Создаем тестовые данные для каждой модели
        self.brand = Brand.objects.create(name='Test Brand')
        self.car = Car.objects.create(brand=self.brand, model='Test Model')
        self.accessories = Accessories.objects.create(name='Test Accessory')
        self.price = Price.objects.create(car=self.car, price=10000)
        self.stock = Stock.objects.create(car=self.car, quantity=10)
        self.order = Order.objects.create(car=self.car, quantity=1)
        self.revoke = Revoke.objects.create(order=self.order, reason='Test Reason')

    def test_brand_creation(self):
        # Проверяем, что бренд был создан с правильным именем
        self.assertEqual(self.brand.name, 'Test Brand')

    def test_car_creation(self):
        # Проверяем, что автомобиль был создан с правильным брендом и моделью
        self.assertEqual(self.car.brand, self.brand)
        self.assertEqual(self.car.model, 'Test Model')

    def test_accessories_creation(self):
        # Проверяем, что аксессуар был создан с правильным именем
        self.assertEqual(self.accessories.name, 'Test Accessory')

    def test_price_creation(self):
        # Проверяем, что цена была создана для правильного автомобиля и с правильной суммой
        self.assertEqual(self.price.car, self.car)
        self.assertEqual(self.price.price, 10000)

    def test_stock_creation(self):
        # Проверяем, что складская запись была создана для правильного автомобиля и с правильным количеством
        self.assertEqual(self.stock.car, self.car)
        self.assertEqual(self.stock.quantity, 10)

    def test_order_creation(self):
        # Проверяем, что заказ был создан для правильного автомобиля и с правильным количеством
        self.assertEqual(self.order.car, self.car)
        self.assertEqual(self.order.quantity, 1)

    def test_revoke_creation(self):
        # Проверяем, что отмена заказа была создана для правильного заказа и с правильной причиной
        self.assertEqual(self.revoke.order, self.order)
        self.assertEqual(self.revoke.reason, 'Test Reason')
