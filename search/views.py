from django.shortcuts import render
import requests
import json


def home(request):
    return render(request, 'home.html')


def search(request):
    return render(request, 'search.html')