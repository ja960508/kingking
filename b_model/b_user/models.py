from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# 기본 유저 모델 사용

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


class Profile(models.Model):
    GENDER_CHOICES = (
        (0, "Male"),
        (1, "Female")
    )
    user = models.OneToOneField(
        User,
        on_delete = models.CASCADE
    )
    gender = models.IntegerField("성별", choices=GENDER_CHOICES)
    subscribed_brand = models.ManyToManyField(
        Shop,
    )

# @receiver(post_save, sender = User)
# def create_user_profile(sender, instance, created, **kwargs):
#         if created:
#             Profile.objects.created(user = instance)

# @receiver(post_save, sender = User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()    


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
# 상품 클래스, 브랜드는 ManytoOne 관계로 한 브랜드에서 여러 개의 상품을 등록할 수 있게 설계했다.


class Order(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete = models.CASCADE
    )
    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE
    )
    quantity = models.IntegerField("수량", default=1) 
    order_data = models.DateTimeField(auto_now_add = True)