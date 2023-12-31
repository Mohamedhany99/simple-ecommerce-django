from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# customized user model


# task number 3
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user.username}"

    class Meta:
        verbose_name = "user profile"
        verbose_name_plural = "user profiles"
        db_table = "user_profiles"


# task number 6
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"
        db_table = "products"


class UserCart(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    products = models.ManyToManyField(Product, related_name="user_cart_products")

    def __str__(self) -> str:
        return f"{self.user}"

    class Meta:
        verbose_name = "user cart"
        verbose_name_plural = "user carts"
        db_table = "user_cart"


class Order(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    cart = models.ForeignKey(UserCart, on_delete=models.SET_NULL, null=True)
    total = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.total}"

    class Meta:
        verbose_name = "order"
        verbose_name_plural = "orders"
        db_table = "orders"
