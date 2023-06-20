from django.contrib.auth.forms import UserCreationForm
# from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth import authenticate, login

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

@api_view(('POST',))
@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            x= login(request, user)
            print(x)
            return Response(data="Logged In",status=status.HTTP_200_OK)
        else:
            print("not logged in")
            return Response(data="cannot login",status=status.HTTP_409_CONFLICT)
