from django.db import models
from django.contrib.auth.models import AbstractUser

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

class User(AbstractUser):
    GENDER_CHOICES = (
        (0, "Male"),
        (1, "Female")
    )
    gender = models.IntegerField("성별", choices = GENDER_CHOICES)
    subscribed_brand = models.ManyToManyField(
        Shop,
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
    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
    )
    product = models.ForeignKey(
        Product,
        on_delete = models.CASCADE
    )