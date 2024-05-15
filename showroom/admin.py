from django.contrib import admin
from .models import Brand, Car, Accessories, Price, Stock, Order, Revoke

admin.site.register(Brand)
admin.site.register(Car)
admin.site.register(Accessories)
admin.site.register(Price)
admin.site.register(Stock)
admin.site.register(Order)
admin.site.register(Revoke)
