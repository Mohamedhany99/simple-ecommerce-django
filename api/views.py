from django.contrib.auth.forms import UserCreationForm
# from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth import authenticate, login
from .models import Product
from .serializers import ListProductSerializer
from rest_framework import filters

#used csrf exempt to exclude the csrf token from postman when tested
#task number 4
@api_view(('POST',))
@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return Response(data="successfuly registered",status=status.HTTP_200_OK)
            # return redirect('login')
        else:
            return Response(data=form.errors,status=status.HTTP_412_PRECONDITION_FAILED)
    else:
        form = UserCreationForm()
#task number 5
@api_view(('POST',))
@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.data['username']
        password = request.data['password']
        print(request.data)
        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            x= login(request, user)
            print(x)
            return Response(data="Logged In",status=status.HTTP_200_OK)
        else:
            print("not logged in")
            return Response(data="cannot login",status=status.HTTP_409_CONFLICT)
#task 7
class ListProductsView(generics.ListAPIView):
    # queryset = Product.objects.all()
    serializer_class = ListProductSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ["name"]

    def get_queryset(self):
        queryset = Product.objects.all().order_by("price")
        return queryset
    #we can use this list built in view to make a get list method or use the generic api view and return serializer.data
    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Exception as e:
            print(e)
            return Response(data="cannot list all the products",status=status.HTTP_409_CONFLICT)