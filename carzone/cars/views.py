from django.shortcuts import render
from pages.models import Team
from cars.models import Car

# Create your views here.


def cars(request):

    all_cars = Car.objects.all()
    data = {"all_cars": all_cars}
    return render(request, "cars/cars.html", data)


def cardetail(request):

    featured_cars = Car.objects.order_by(
        "created_date").filter(is_featured=True)
    data = {

        "featured_cars": featured_cars,

    }
    return render(request, "cars/cars-detail.html", data)
