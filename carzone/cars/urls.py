from django.urls import path
from.import views
app_name = "cars"
urlpatterns = [
    path("", views.cars, name="cars"),
    path("detail/",views.cardetail,name="cardetail")


]
