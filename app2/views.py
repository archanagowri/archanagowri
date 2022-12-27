from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def second(request):
    return HttpResponse('<h1><marquee><font color=green>This is App2 Views</font></marquee></h1>')