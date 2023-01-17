from django.utils.html import format_html
from django.contrib import admin
from.models import Car
# Register your models here.


class CarAdmin(admin.ModelAdmin):
    def thumnail(self, object):
        return format_html('<img src="{}" width="40" style="border_radius:"50px"/>'.format(object.car_photo.url))

    list_display = ("id", "car_title",
                    "model", "year", "is_featured")
    list_display_links = ("id", "car_title")
    list_editable = ("is_featured",)
    search_fields = ("id", "car_title", "city", "body_style")
    list_filter = ("city", "model", "body_style")


admin.site.register(Car, CarAdmin)
