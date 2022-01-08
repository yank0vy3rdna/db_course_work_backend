from django.contrib import admin

# Register your models here.
from django.utils.html import format_html
from django.urls import reverse
from django.utils.http import urlencode

from .models import PERSONAL_DATA, PLACE, EXHIBIT, EXHIBITION, MUSEUM, PASSPORT, GUIDE, EXCURSIONIST, EXCURSION, \
    DOCUMENT_STATUS, GROUP, DOCUMENT_ACCREDITATION


@admin.register(PERSONAL_DATA)
class PERSONAL_DATA(admin.ModelAdmin):
    list_display = ("id",
                    "SURNAME",
                    "NAME",
                    "PATRONYMIC",
                    "GENDER",
                    "DATE_BIRTHDAY")
    search_fields = ("id",
                     "SURNAME",
                     "NAME",
                     "PATRONYMIC",
                     "GENDER")


@admin.register(PLACE)
class PLACE(admin.ModelAdmin):
    list_display = ("id",
                    "COUNTRY",
                    "CITY",
                    "STREET",
                    "HOUSE")
    search_fields = ("id",
                     "COUNTRY",
                     "CITY",
                     "STREET",
                     "HOUSE")
    list_filter = ('COUNTRY', 'CITY')


@admin.register(EXHIBIT)
class EXHIBIT(admin.ModelAdmin):
    list_display = ("id",
                    "NAME",
                    "AUTHOR",
                    "DATE_CREATION",
                    "DIRECTION",
                    "LOCATION")
    search_fields = ("id",
                     "NAME",
                     "AUTHOR",
                     "LOCATION")
    list_filter = ('AUTHOR', 'DATE_CREATION')


@admin.register(EXHIBITION)
class EXHIBITION(admin.ModelAdmin):
    list_display = ("id",
                    "NAME",
                    "Owner",
                    "Location")
    search_fields = ("id",
                     "NAME",
                     "OWNER",
                     "LOCATION")
    list_filter = ('OWNER', 'LOCATION')
    filter_horizontal = ('exhibit',)

    def Owner(self, obj):
        return obj.id

    Owner.short_description = "OWNER"

    def Location(self, obj):
        id = obj.id
        # url = (
        #     reverse("admin:db_course_work_backend_places_changelist")
        # )
        # return format_html('<a href="{}">ID_LOCATION {}</a>', url, id)
        return obj.id

    Location.short_description = "LOCATION"


# todo
@admin.register(MUSEUM)
class MUSEUM(admin.ModelAdmin):
    list_display = ("NAME",
                    "LOCATION")


@admin.register(PASSPORT)
class PASSPORT(admin.ModelAdmin):
    list_display = (
        "SERIES_PASSPORT",
        "NUMBER_PASSPORT",
        "SURNAME",
        "NAME",
        "PATRONYMIC",
        "GENDER",
        "DATE_BIRTHDAY",
        "PASSPORT_ISSUE",
        "DATE_ISSUE")


@admin.register(GUIDE)
class GUIDE(admin.ModelAdmin):
    list_display = ("MOBILE_NUMBER",
                    "PASSPORT_ID",
                    "EMAIL")


@admin.register(EXCURSIONIST)
class EXCURSIONIST(admin.ModelAdmin):
    list_display = ("HUMAN",
                    "MOBILE_NUMBER",
                    "EMAIL")


@admin.register(EXCURSION)
class EXCURSION(admin.ModelAdmin):
    list_display = ("NAME",
                    "DESCRIPTION",
                    "DURATION")


@admin.register(DOCUMENT_STATUS)
class DOCUMENT_STATUS(admin.ModelAdmin):
    list_display = ("INSTITUTION",
                    "NAME",
                    "DATE_ISSUE",
                    "DATE_CANCELLATION")


@admin.register(GROUP)
class GROUP(admin.ModelAdmin):
    list_display = ("EXHIBITION_ID",
                    "GUIDE",
                    "TIME",
                    "COST",
                    "NUMBER_SEATS",
                    "PLACE_GATHERING",
                    "PLACE_TERMINATION")


@admin.register(DOCUMENT_ACCREDITATION)
class DOCUMENT_ACCREDITATION(admin.ModelAdmin):
    list_display = ("INSTITUTION",
                    "NAME",
                    "DATE_ISSUE",
                    "DATE_CANCELLATION")
