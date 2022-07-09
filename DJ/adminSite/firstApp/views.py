from django.shortcuts import render
from .models import Login

# Create your views here.

def index(request):
    customers = Login.objects.all()
    return render(request, 'firstApp/index.html', 
    {
        "customerDetails": customers
    })
