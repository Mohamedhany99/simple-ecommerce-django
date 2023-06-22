"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api.views import (
    register,
    login_view,
    ListProductsView,
    UserRegister,
    UserLogin,
    AddToCartView,
    UserViewCart,
    MakeOrder,
    ViewOrders,
)
from rest_framework_simplejwt import views as jwt_views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    # admin panel url
    path("admin/", admin.site.urls),
    # jwt authentication tokens
    path(
        "api/token/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),
    path(
        "api/token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"
    ),
    # swagger docs api
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="docs"),
    # api tasks docs
    path("register/", UserRegister.as_view(), name="register"),
    path("login/", UserLogin.as_view(), name="login"),
    path("products/", ListProductsView.as_view(), name="list-products"),
    path("add-cart/", AddToCartView.as_view(), name="add-to-cart"),
    path("user-cart/", UserViewCart.as_view(), name="view-cart"),
    path("make-order/", MakeOrder.as_view(), name="make-order"),
    path("view-order/", ViewOrders.as_view(), name="view-order"),
]
