from django.contrib import admin
from .models import Shop, Product, Order, Profile
# Register your models here.

admin.site.register(Shop)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Profile)