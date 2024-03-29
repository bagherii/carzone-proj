from django.db import models
from datetime import datetime
from multiselectfield import MultiSelectField
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField
# Create your models here.


class Car(models.Model):
    state_choice = (("al", "alabama"),
                    ("ak", "alaska"),
                    ("wy", "wyoming"),

                    ("wi", "wisconsin")
                    )

    year_choice = []
    for r in range(2000, (datetime.now().year+1)):
        year_choice.append((r, r))

    features_choices = (
        ("cruise control", "cruis control"),
        ("audio interface", "audio interface"),
        ("alarm syste", "malarm system"),
        ("seat heatin", "seat heating"),


    )
    door_choices = (
        ("4", "4"),
        ("5", "5"),
        ("3", "3"),
        ("6", "6")
    )

    car_title = models.CharField(max_length=255)
    state = models.CharField(choices=state_choice, max_length=100)
    city = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(("year"), choices=year_choice)
    condition = models.CharField(max_length=100)
    price = models.IntegerField()
    description = RichTextField()
    car_photo_1 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    car_photo3 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    car_photo_4 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    features = MultiSelectField(choices=features_choices, max_length=100)
    body_style = models.CharField(max_length=100)
    engin = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    interior = models.CharField(max_length=100)
    miles = models.IntegerField()
    doors = models.CharField(choices=door_choices, max_length=100)
    passengers = models.IntegerField()
    vin_o = models.CharField(max_length=100)
    milage = models.CharField(max_length=100)
    fuel_type = models.CharField(max_length=50)
    no_of_owners = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(datetime.now, blank=True)

    def __str__(self):
        return self.car_title
