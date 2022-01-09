from django.contrib import admin

# Register your models here.
from django.utils.html import format_html
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.safestring import mark_safe

from .models import PERSONAL_DATA, PLACE, EXHIBIT, EXHIBITION, MUSEUM, PASSPORT, GUIDE, EXCURSIONIST, EXCURSION, \
    DOCUMENT_STATUS, GROUP, DOCUMENT_ACCREDITATION


@admin.register(PERSONAL_DATA)
class PERSONAL_DATA(admin.ModelAdmin):
    list_display = ("id",
                    "SURNAME",
                    "NAME",
                    "PATRONYMIC",
                    "GENDER",
                    "DATE_BIRTHDAY",
                    "USER_ID")
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
                    "Author",
                    "DATE_CREATION",
                    "DIRECTION",
                    "Location")
    search_fields = ("id",
                     "NAME",)
    list_filter = ('AUTHOR', 'DATE_CREATION')

    def Author(self, obj):
        return obj.id

    Author.short_description = "AUTHOR"

    def Location(self, obj):
        return obj.id
        # return format_html('<a href="{}"> ID: {}</a>',
        #                    (reverse("db_course_work_backend_exhibit_changelist")),
        #                    obj.id)
        # https://pythonist.ru/kastomizacziya-admin-paneli-django/

    Location.short_description = "LOCATION"


@admin.register(EXHIBITION)
class EXHIBITION(admin.ModelAdmin):
    list_display = ("id",
                    "NAME",
                    "Owner",
                    "Location")
    search_fields = ("id",
                     "NAME",)
    list_filter = ('OWNER', 'LOCATION')
    filter_horizontal = ('exhibit',)

    def Owner(self, obj):
        return mark_safe(f"<a href='/admin/db_course_work_backend/personal_data/{obj.id}/change/'>{obj.id}</a>")

    Owner.short_description = "OWNER"

    def Location(self, obj):
        return obj.id

    Location.short_description = "LOCATION"


@admin.register(MUSEUM)
class MUSEUM(admin.ModelAdmin):
    list_display = ("id",
                    "NAME",
                    "Location")
    search_fields = ("id",
                     "NAME",)
    list_filter = ('LOCATION',)
    filter_horizontal = ('exhibition',)

    def Location(self, obj):
        return obj.id

    Location.short_description = "LOCATION"


@admin.register(PASSPORT)
class PASSPORT(admin.ModelAdmin):
    list_display = ("id",
                    "SERIES_PASSPORT",
                    "NUMBER_PASSPORT",
                    "SURNAME",
                    "NAME",
                    "PATRONYMIC",
                    "GENDER",
                    "DATE_BIRTHDAY",
                    "PASSPORT_ISSUE",
                    "DATE_ISSUE")

    search_fields = ("id",
                     "SERIES_PASSPORT",
                     "NUMBER_PASSPORT",
                     "SURNAME",
                     "NAME",
                     "PATRONYMIC",
                     "GENDER")
    list_filter = ("DATE_BIRTHDAY",
                   "PASSPORT_ISSUE",
                   "DATE_ISSUE",)


@admin.register(GUIDE)
class GUIDE(admin.ModelAdmin):
    list_display = ("id",
                    "MOBILE_NUMBER",
                    "PASSPORT_id",
                    "EMAIL",
                    "USER_ID")
    search_fields = ("id",
                     "MOBILE_NUMBER",
                     "EMAIL",)

    def PASSPORT_id(self, obj):
        return obj.id

    PASSPORT_id.short_description = "PASSPORT_ID"


@admin.register(EXCURSIONIST)
class EXCURSIONIST(admin.ModelAdmin):
    list_display = ("id",
                    "Human",
                    "MOBILE_NUMBER",
                    "EMAIL")
    search_fields = ("id",
                     "MOBILE_NUMBER",
                     "EMAIL",)

    def Human(self, obj):
        return obj.id

    Human.short_description = "HUMAN"


@admin.register(EXCURSION)
class EXCURSION(admin.ModelAdmin):
    list_display = ("id",
                    "NAME",
                    "DESCRIPTION",
                    "DURATION")
    search_fields = ("id",
                     "NAME",
                     "DESCRIPTION",)
    list_filter = ('DURATION',)
    filter_horizontal = ('museum',
                         'exhibition',
                         'exhibit',)


@admin.register(DOCUMENT_STATUS)
class DOCUMENT_STATUS(admin.ModelAdmin):
    list_display = ("id",
                    "INSTITUTION",
                    "NAME",
                    "DATE_ISSUE",
                    "DATE_CANCELLATION")
    search_fields = ("id",
                     "INSTITUTION",
                     "NAME")
    list_filter = ("DATE_ISSUE",
                   "DATE_CANCELLATION",)
    filter_horizontal = ('excursionist',)


@admin.register(GROUP)
class GROUP(admin.ModelAdmin):
    list_display = ("id",
                    "EXHIBITION_id",
                    "Guide",
                    "TIME",
                    "COST",
                    "NUMBER_SEATS",
                    "Place_gathering",
                    "Place_termination")

    search_fields = ("id",
                     "TIME",
                     "COST",
                     "NUMBER_SEATS")
    list_filter = ('PLACE_GATHERING',
                   'PLACE_TERMINATION',)
    filter_horizontal = ('excursionist',)

    def EXHIBITION_id(self, obj):
        return obj.id

    EXHIBITION_id.short_description = "EXHIBITION_ID"

    def Guide(self, obj):
        return obj.id

    Guide.short_description = "GUIDE"

    def Place_gathering(self, obj):
        return obj.id

    Place_gathering.short_description = "PLACE_GATHERING"

    def Place_termination(self, obj):
        return obj.id

    Place_termination.short_description = "PLACE_TERMINATION"


@admin.register(DOCUMENT_ACCREDITATION)
class DOCUMENT_ACCREDITATION(admin.ModelAdmin):
    list_display = ("id",
                    "INSTITUTION",
                    "NAME",
                    "DATE_ISSUE",
                    "DATE_CANCELLATION")

    search_fields = ("id",
                     "INSTITUTION",
                     "NAME",)
    list_filter = ("DATE_ISSUE",
                   "DATE_CANCELLATION",)
    filter_horizontal = ('guide',)
