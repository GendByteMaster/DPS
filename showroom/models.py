from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Car(models.Model):
    model = models.CharField(max_length=100)
    engine_capacity = models.DecimalField(max_digits=5, decimal_places=2)
    doors = models.IntegerField()
    color = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.IntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.model} ({self.year})"

class Accessories(models.Model):
    name = models.CharField(max_length=100)
    additional_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Price(models.Model):
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    accessories = models.ManyToManyField(Accessories)

    def calculate_total_price(self):
        return self.base_price + sum(acc.additional_price for acc in self.accessories.all())

    def __str__(self):
        return f"Base Price: {self.base_price}"

class Stock(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    is_reserved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.car.model} - {'Reserved' if self.is_reserved else 'Available'}"

class Order(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    price = models.ForeignKey(Price, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order for {self.car.model} on {self.date}"

class Revoke(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Revoke order for {self.order.car.model} on {self.date}"
