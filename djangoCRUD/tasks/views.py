from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from djangoCRUD.serializers import UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.shortcuts import get_object_or_404

from django.contrib.auth.models import User





# Create your views here.
def signupPage(request):
    return render(request, 'signup.html')


def homePage(request):
    return render(request, 'home.html')


def registerPage(request):
    return render(request, 'register.html')

