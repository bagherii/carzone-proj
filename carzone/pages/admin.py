from django.utils.html import format_html
from django.contrib import admin
from.models import Team
# Register your models here.


class TeamAdmin(admin.ModelAdmin):
    def thumnail(self, object):
        return format_html('<img  src="{}" width="40" style="border-radius:50px "/>'.format(object.photo.url))
    thumnail.short_description = "photo"
    list_display = ("id", "first_name",
                    "last_name", "created_date")
    list_display_links = ("id", "first_name")
    search_fields = ("first_name", "last_name", "designation")
    list_filter = ("designation",)


admin.site.register(Team, TeamAdmin)
