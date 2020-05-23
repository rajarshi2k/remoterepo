from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homeview(request):
    return HttpResponse("<h1> great raja</h1>")