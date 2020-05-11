from django.db import models

# Create your models here.

SIZE_CHOICES = (
    (0, 'S'),
    (1, 'M'),
    (2, 'L'),
    (3, 'XL'),
    (4, 'XXL')
)

CATEGORY_CHOICES = (
    (0, 'shoes'),
    (1, 'outer'),
    (2, 'pants'),
    (3, 'top'),
    (4, 'accesary')
)

class Shop(models.Model):
    name = models.CharField(max_length = 128)

    def __self__(self):
        return self.name


class Product(models.Model):
    brand = models.ForeignKey(
        Shop,
        on_delete = models.CASCADE,
        )
    name= models.CharField(max_length = 64, verbose_name = "품명")
    price = models.IntegerField("가격")
    size = models.IntegerField(choices = SIZE_CHOICES)
    category = models.IntegerField(choices = CATEGORY_CHOICES)
    
    def __self__(self):
        return self.name


class Order(models.Model):