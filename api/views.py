from django.contrib.auth.forms import UserCreationForm

# from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Product, UserCart, Order, UserProfile
from .serializers import (
    ListProductSerializer,
    AddToCartSerializer,
    OrderSerializer,
    UserRegisterationSerializer,
    LoginSerializer,
)
from rest_framework import filters
from django.shortcuts import get_object_or_404
from .tokens import get_tokens_for_user


# used csrf exempt to exclude the csrf token from postman when tested
# task number 4
class UserRegister(generics.GenericAPIView):
    serializer_class = UserRegisterationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                data=serializer.validated_data, status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                data=serializer.errors, status=status.HTTP_412_PRECONDITION_FAILED
            )


# this is not used I am using the above make it using DRF
@api_view(("POST",))
@csrf_exempt
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return Response(data="successfuly registered", status=status.HTTP_200_OK)
            # return redirect('login')
        else:
            return Response(
                data=form.errors, status=status.HTTP_412_PRECONDITION_FAILED
            )
    else:
        form = UserCreationForm()


# task number 5
class UserLogin(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = get_object_or_404(User, username=username)
        if user is not None:
            if user.check_password(raw_password=password):
                tokens = get_tokens_for_user(user=user)
                serializer = self.serializer_class(instance=user)
                data = {
                    "username": serializer.data["username"],
                    "tokens": tokens,
                }
                return Response(data=data, status=status.HTTP_200_OK)
        else:
            return Response(
                data="cannot find user info", status=status.HTTP_404_NOT_FOUND
            )


# this is not used and replaced with the above make it using DRF
@api_view(("POST",))
@csrf_exempt
def login_view(request):
    if request.method == "POST":
        username = request.data["username"]
        password = request.data["password"]
        print(request.data)
        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            x = login(request, user)
            print(x)
            return Response(data="Logged In", status=status.HTTP_200_OK)
        else:
            print("not logged in")
            return Response(data="cannot login", status=status.HTTP_409_CONFLICT)


# task 7
class ListProductsView(generics.ListAPIView):
    # queryset = Product.objects.all()
    serializer_class = ListProductSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ["name"]
    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        queryset = Product.objects.all().order_by("price")
        return queryset

    # we can use this list built in view to make a get list method or use the generic api view and return serializer.data
    def list(self, request, *args, **kwargs):
        try:
            # print(request.user)
            return super().list(request, *args, **kwargs)
        except Exception as e:
            print(e)
            return Response(
                data="cannot list all the products", status=status.HTTP_409_CONFLICT
            )


# task 8
class AddToCartView(generics.GenericAPIView):
    serializer_class = AddToCartSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        print(request.data)
        mutable_dict = request.data.copy()
        print(request.user)
        mutable_dict["user"] = get_object_or_404(UserProfile, user=request.user).pk
        print(mutable_dict)
        serializer = self.serializer_class(data=mutable_dict)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_409_CONFLICT)
