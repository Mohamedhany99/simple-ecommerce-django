from rest_framework import serializers
from .models import Product, UserCart, Order
from django.contrib.auth.models import User
from django.contrib.auth import password_validation


# registeration for auth.users
class UserRegisterationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(
        max_length=150, required=True, write_only=True
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password",
            "confirm_password",
        )
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, attr: dict):
        password = attr.get("password")
        confirm_password = attr.get("confirm_password")
        if password != confirm_password:
            raise serializers.ValidationError(
                detail={"password": ["Passwords missmatch."]}, code=400
            )
        return attr

    def validate_password(self, value):
        if value:
            password_validation.validate_password(value)
        return value

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data.get("username"),
            email=validated_data.get("email"),
        )
        user.set_password(validated_data.get("password"))
        user.save()
        return user


# login serializer
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "password",
        )


class ListProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "name",
            "price",
        ]
        ordering = "-price"


class AddToCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCart
        fields = [
            "user",
            "products",
        ]

    def create(self, validated_data):
        print("validated data =", validated_data)
        products = validated_data.pop("products")
        print("**validated data:", validated_data["user"])
        cart = UserCart.objects.create(user=validated_data["user"])
        cart.products.set(products)
        return cart


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "user",
            "cart",
            "total",
        ]
