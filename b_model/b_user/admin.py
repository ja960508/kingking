from django.contrib import admin
from .models import Shop, User, Product, Order
# Register your models here.

admin.site.register(Shop)
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Order)