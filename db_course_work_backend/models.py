from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator


# Create your models here.
class PERSONAL_DATA(models.Model):
    SURNAME = models.CharField(max_length=45)
    NAME = models.CharField(max_length=45)
    PATRONYMIC = models.CharField(max_length=45)
    GENDER = models.BooleanField(null=False)
    DATE_BIRTHDAY = models.DateTimeField()
    USER_ID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Personal data'
        verbose_name_plural = 'Personal data'


class PLACE(models.Model):
    COUNTRY = models.CharField(max_length=90)
    CITY = models.CharField(max_length=90)
    STREET = models.CharField(max_length=90)
    HOUSE = models.IntegerField(null=True)


class EXHIBIT(models.Model):
    NAME = models.CharField(max_length=90, default="МАДОННА С МЛАДЕНЦЕМ")
    AUTHOR = models.ForeignKey(PERSONAL_DATA, null=False, on_delete=models.DO_NOTHING)
    DATE_CREATION = models.DateTimeField()
    DIRECTION = models.CharField(max_length=45)
    LOCATION = models.ForeignKey(PLACE, null=False, on_delete=models.DO_NOTHING)


class EXHIBITION(models.Model):
    NAME = models.CharField(max_length=90)
    OWNER = models.ForeignKey(PERSONAL_DATA, null=True, on_delete=models.DO_NOTHING)
    LOCATION = models.ForeignKey(PLACE, null=False, on_delete=models.CASCADE)
    exhibit = models.ManyToManyField(EXHIBIT)


class MUSEUM(models.Model):
    NAME = models.CharField(max_length=90)
    LOCATION = models.ForeignKey(PLACE, null=False, on_delete=models.CASCADE)
    exhibition = models.ManyToManyField(EXHIBITION)


class PASSPORT(models.Model):
    SERIES_PASSPORT = models.IntegerField()
    NUMBER_PASSPORT = models.IntegerField(null=True)
    SURNAME = models.CharField(max_length=45)
    NAME = models.CharField(max_length=45)
    PATRONYMIC = models.CharField(max_length=45)
    GENDER = models.BooleanField(null=False)
    DATE_BIRTHDAY = models.DateTimeField()
    PASSPORT_ISSUE = models.CharField(max_length=200)
    DATE_ISSUE = models.DateTimeField()


class GUIDE(models.Model):
    MOBILE_NUMBER = models.BigIntegerField(null=False)
    PASSPORT_ID = models.ForeignKey(PASSPORT, null=False, on_delete=models.CASCADE)
    EMAIL = models.CharField(max_length=45, unique=True)
    USER_ID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class EXCURSIONIST(models.Model):
    HUMAN = models.ForeignKey(PERSONAL_DATA, null=True, on_delete=models.CASCADE)
    MOBILE_NUMBER = models.CharField(max_length=45)
    EMAIL = models.CharField(max_length=45)


class EXCURSION(models.Model):
    NAME = models.CharField(max_length=90)
    DESCRIPTION = models.CharField(max_length=400,
                                   default="Самая незабываемая и интересная экскурсия, которую можно посетить.")
    DURATION = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(24)])
    museum = models.ManyToManyField(MUSEUM)
    exhibition = models.ManyToManyField(EXHIBITION)
    exhibit = models.ManyToManyField(EXHIBIT)


class DOCUMENT_STATUS(models.Model):
    INSTITUTION = models.CharField(max_length=180, null=True)
    NAME = models.CharField(max_length=180)
    DATE_ISSUE = models.DateTimeField()
    DATE_CANCELLATION = models.DateTimeField()
    excursionist = models.ManyToManyField(EXCURSIONIST)

    class Meta:
        verbose_name = 'Document status'
        verbose_name_plural = 'Document status'


class GROUP(models.Model):
    EXCURSION_ID = models.ForeignKey(EXCURSION, null=False, on_delete=models.CASCADE)
    GUIDE = models.ForeignKey(GUIDE, null=False, on_delete=models.CASCADE)
    TIME = models.DateTimeField()
    COST = models.IntegerField()
    NUMBER_SEATS = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(21)])
    PLACE_GATHERING = models.ForeignKey(PLACE, related_name="PLACE_GATHERING", null=False, on_delete=models.CASCADE)
    PLACE_TERMINATION = models.ForeignKey(PLACE, related_name="PLACE_TERMINATION", null=False, on_delete=models.CASCADE)
    excursionist = models.ManyToManyField(EXCURSIONIST)


class DOCUMENT_ACCREDITATION(models.Model):
    INSTITUTION = models.CharField(max_length=180, null=True)
    NAME = models.CharField(max_length=180)
    DATE_ISSUE = models.DateTimeField()
    DATE_CANCELLATION = models.DateTimeField()
    guide = models.ManyToManyField(GUIDE)

    class Meta:
        verbose_name = 'Document accreditation'
        verbose_name_plural = 'Document accreditation'
