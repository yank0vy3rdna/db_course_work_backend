from django.contrib import admin

# Register your models here.
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
    list_filter = ('COUNTRY',
                   'CITY')


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
        return mark_safe(f"<a href='/admin/db_course_work_backend/personal_data/{obj.AUTHOR_id}/change/'>{obj.AUTHOR_id}</a>")

    Author.short_description = "AUTHOR"

    def Location(self, obj):
        return mark_safe(f"<a href='/admin/db_course_work_backend/place/{obj.LOCATION_id}/change/'>{obj.LOCATION_id}</a>")

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
        return mark_safe(f"<a href='/admin/db_course_work_backend/personal_data/{obj.OWNER_id}/change/'>{obj.OWNER_id}</a>")

    Owner.short_description = "OWNER"

    def Location(self, obj):
        return mark_safe(f"<a href='/admin/db_course_work_backend/place/{obj.LOCATION_id}/change/'>{obj.LOCATION_id}</a>")

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
        return mark_safe(f"<a href='/admin/db_course_work_backend/place/{obj.LOCATION_id}/change/'>{obj.LOCATION_id}</a>")

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
        return mark_safe(f"<a href='/admin/db_course_work_backend/passport/{obj.PASSPORT_ID_id}/change/'>{obj.PASSPORT_ID_id}</a>")

    PASSPORT_id.short_description = "PASSPORT_ID"


@admin.register(EXCURSIONIST)
class EXCURSIONIST(admin.ModelAdmin):
    list_display = ("id",
                    "Human",
                    "MOBILE_NUMBER",
                    "EMAIL",
                    "USER_id")
    search_fields = ("id",
                     "MOBILE_NUMBER",
                     "EMAIL",)

    def Human(self, obj):
        return mark_safe(f"<a href='/admin/db_course_work_backend/personal_data/{obj.HUMAN_id}/change/'>{obj.HUMAN_id}</a>")

    Human.short_description = "PERSONAL DATA"

    def USER_id(self, obj):
        return mark_safe(f"<a href='/admin/auth/user/{obj.USER_ID_id}/change/'>{obj.USER_ID_id}</a>")

    USER_id.short_description = "USER ID"


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
                    "EXCURSION_id",
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

    def EXCURSION_id(self, obj):
        return mark_safe(f"<a href='/admin/db_course_work_backend/exhibition/{obj.EXCURSION_ID_id}/change/'>{obj.EXCURSION_ID_id}</a>")

    EXCURSION_id.short_description = "EXCURSION_ID"

    def Guide(self, obj):
        return mark_safe(f"<a href='/admin/db_course_work_backend/guide/{obj.GUIDE_id}/change/'>{obj.GUIDE_id}</a>")

    Guide.short_description = "GUIDE"

    def Place_gathering(self, obj):
        return mark_safe(f"<a href='/admin/db_course_work_backend/place/{obj.PLACE_GATHERING_id}/change/'>{obj.PLACE_GATHERING_id}</a>")

    Place_gathering.short_description = "PLACE_GATHERING"

    def Place_termination(self, obj):
        return mark_safe(f"<a href='/admin/db_course_work_backend/place/{obj.PLACE_TERMINATION_id}/change/'>{obj.PLACE_TERMINATION_id}</a>")

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
