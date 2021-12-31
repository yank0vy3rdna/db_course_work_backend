from django.db import models


# Create your models here.
class PERSONAL_DATA(models.Model):
    SURNAME = models.CharField(max_length=45)
    NAME = models.CharField(max_length=45)
    PATRONYMIC = models.CharField(max_length=45)
    GENDER = models.BooleanField(null=False)
    DATE_BIRTHDAY = models.DateTimeField()


class PLACE(models.Model):
    COUNTRY = models.CharField(max_length=90)
    CITY = models.CharField(max_length=90)
    STREET = models.CharField(max_length=90)
    HOUSE = models.IntegerField(null=True)


class EXHIBIT(models.Model):
    NAME = models.CharField(max_length=90, default="МАДОННА С МЛАДЕНЦЕМ")
    AUTHOR = models.ForeignKey(PERSONAL_DATA, null=False)
    DATE_CREATION = models.DateTimeField()
    DIRECTION = models.CharField(max_length=45)
    LOCATION = models.ForeignKey(PLACE, null=False)


class EXHIBITION(models.Model):
    NAME = models.CharField(max_length=90)
    OWNER = models.ForeignKey(PERSONAL_DATA, null=True)
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
    DATE_BIRTHDAY = models.DateTimeField()  # TODO CHECK ( ДАТА_РОЖДЕНИЯ > '1940-01-01' )
    PASSPORT_ISSUE = models.CharField(max_length=200)
    DATE_ISSUE = models.DateTimeField()  # TODO CHECK ( ДАТА_ВЫДАЧИ > '1960-01-01' )


class GUIDE(models.Model):
    MOBILE_NUMBER = models.BigIntegerField(null=False)  # TODO CHECK ( МОБИЛЬНЫЙ_НОМЕР::text ~ '^[0-9]{10}$' )
    PASSPORT_ID = models.ForeignKey(PASSPORT, null=False, on_delete=models.CASCADE)
    EMAIL = models.CharField(max_length=45, unique=True)  # TODO CHECK (ПОЧТА ~ '^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$')


class EXCURSIONIST(models.Model):
    HUMAN = models.ForeignKey(PERSONAL_DATA, null=True, on_delete=models.CASCADE)
    MOBILE_NUMBER = models.CharField(max_length=45)
    EMAIL = models.CharField(max_length=45)


class EXCURSION(models.Model):
    NAME = models.CharField(max_length=90)
    DESCRIPTION = models.CharField(max_length=400,
                                   default="Самая незабываемая и интересная экскурсия, которую можно посетить.")
    DURATION = models.IntegerField(null=False)  # TODO CHECK ( ПРОДОЛЖИТЕЛЬНОСТЬ < 23 )
    museum = models.ManyToManyField(MUSEUM)
    exhibition = models.ManyToManyField(EXHIBITION)
    exhibit = models.ManyToManyField(EXHIBIT)


class DOCUMENT_STATUS(models.Model):
    INSTITUTION = models.CharField(max_length=180, null=True)
    NAME = models.CharField(max_length=180)
    DATE_ISSUE = models.DateTimeField()  # TODO CHECK ( ДАТА_ВЫДАЧИ > '1940-01-01' )
    DATE_CANCELLATION = models.DateTimeField()
    excursionist = models.ManyToManyField(EXCURSIONIST)


class GROUP(models.Model):
    EXHIBITION_ID = models.ForeignKey(EXCURSION, null=False, on_delete=models.CASCADE)
    GUIDE = models.ForeignKey(GUIDE, null=False, on_delete=models.CASCADE)
    TIME = models.DateTimeField()
    COST = models.IntegerField()
    NUMBER_SEATS = models.IntegerField()  # TODO CHECK ( КОЛИЧЕСТВО_МЕСТ < 20 )
    PLACE_GATHERING = models.ForeignKey(PLACE, null=False, on_delete=models.CASCADE)
    PLACE_TERMINATION = models.ForeignKey(PLACE, null=False, on_delete=models.CASCADE)
    excursionist = models.ManyToManyField(EXCURSIONIST)


class DOCUMENT_ACCREDITATION(models.Model):
    INSTITUTION = models.CharField(max_length=180, null=True)
    NAME = models.CharField(max_length=180)
    DATE_ISSUE = models.DateTimeField()  # TODO CHECK ( ДАТА_ВЫДАЧИ > '2010-01-01' )
    DATE_CANCELLATION = models.DateTimeField()
    guide = models.ManyToManyField(GUIDE)
