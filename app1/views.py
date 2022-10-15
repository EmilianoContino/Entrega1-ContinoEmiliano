from django.shortcuts import render
from django import http
from django.http import HttpResponse
from django.template import context, loader
from datetime import datetime
from django.shortcuts import render



def index(request):
    return render (request, 'app1/index.html')
