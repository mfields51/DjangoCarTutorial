from django.shortcuts import render
from .models import Car

# Create your views here.
def showcars(request):
    cars = Car.objects.all()
    return render(request, "index.html", {"cars_key": cars})