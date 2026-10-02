from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse




def my_view(request):
    # View code here...
    return render(
        request,
        "main/index.html",

    )