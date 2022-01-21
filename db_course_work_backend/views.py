import json
import smtplib
# Добавляем необходимые подклассы - MIME-типы
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from types import SimpleNamespace

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db import IntegrityError
from django.db.models import QuerySet
from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseBadRequest
# Общие функции(без логина)
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import permission_classes
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from db_course_work_backend.models import GROUP, PERSONAL_DATA, EXCURSIONIST, EXCURSION
from db_course_work_backend.serializers import SmallExcursionSerializer, FullExcursionSerializer, GroupSerializer


class ExcursionListView(ListAPIView):
    authentication_classes = []
    permission_classes = []
    queryset = EXCURSION.objects.all()
    serializer_class = SmallExcursionSerializer


class ExcursionView(RetrieveAPIView):
    authentication_classes = []
    permission_classes = []
    queryset = EXCURSION.objects.all()
    serializer_class = FullExcursionSerializer


def become_guide(request):
    # Получаем данные
    x = json.loads(request.body, object_hook=lambda d: SimpleNamespace(**d))
    mobile_number = x.mobile_number
    email_guide = x.email_guide
    series_passport = x.series_passport
    number_passport = x.number_passport
    surname = x.surname
    name = x.name
    patronymic = x.patronymic
    gender = x.gender
    date_birthday = x.date_birthday
    passport_issue = x.passport_issue
    date_issue = x.date_issue

    # Проверяем заполненность полей
    if mobile_number is None or series_passport is None \
            or number_passport is None or surname is None \
            or name is None or patronymic is None or gender is None \
            or date_birthday is None or passport_issue is None or date_issue is None:
        return HttpResponseBadRequest("<h2>BROKEN DATA</h2>")

    msg_subject = 'Хочу захватить Казахстан'
    body = "mobile_number: " + str(mobile_number) + "\n" + \
           "email" + str(email_guide) + "\n" + \
           "series_passport: " + str(series_passport) + "\n" + \
           "number_passport: " + str(number_passport) + "\n" + \
           "surname: " + str(surname) + "\n" + \
           "name: " + str(name) + "\n" + \
           "patronymic: " + str(patronymic) + "\n" + \
           "gender: " + str(gender) + "\n" + \
           "date_birthday: " + str(date_birthday) + "\n" + \
           "passport_issue: " + str(passport_issue) + "\n" + \
           "date_issue: " + str(date_issue) + "\n"

    status = message_email(msg_subject, body)

    return HttpResponse(status)


@csrf_exempt
def register_become_random_dick(request):
    # Получаем данные
    x = json.loads(request.body, object_hook=lambda d: SimpleNamespace(**d))
    username = x.username
    password = x.password
    mobile_number = x.mobile_number
    email = x.email
    surname = x.surname
    name = x.name
    patronymic = x.patronymic
    gender = x.gender
    date_birthday = x.date_birthday

    if username is None or password is None \
            or mobile_number is None or email is None \
            or surname is None and name is None \
            and patronymic is None and gender is None \
            and date_birthday is None:
        return HttpResponseBadRequest("<h2>BROKEN DATA</h2>")

    try:
        new_user = User.objects.create_user(username=username)
        new_user.set_password(str(password))
        new_user.save()
    except IntegrityError:
        return HttpResponseBadRequest("<h2>Пользователь с таким именем уже существует</h2>")

    try:
        new_user.groups.add(3)
    except IntegrityError:
        return HttpResponseBadRequest("<h2>К сожалению проблемы с группой прав для вас</h2>")

    new_personal_data = PERSONAL_DATA.objects.create(SURNAME=surname, NAME=name, PATRONYMIC=patronymic, GENDER=gender,
                                                     DATE_BIRTHDAY=date_birthday)
    EXCURSIONIST.objects.create(MOBILE_NUMBER=mobile_number, EMAIL=email, USER_ID_id=new_user.id,
                                HUMAN_id=new_personal_data.id)

    return HttpResponse('OK')


# Гид функции
def stub_add_accreditation(request):
    return add_status_or_accreditation(request)


class AddToGroupView(View):
    login_required = True
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user, _ = JWTAuthentication().authenticate(request)
        if not user.is_authenticated:
            return HttpResponse('Unauthorized', status=401)
        group_id = request.GET.get("group_id", 1)
        user_id = user.id

        if group_id is None or user_id is None:
            return HttpResponseBadRequest("<h2>BROKEN DATA</h2>")

        group = GROUP.objects.get(id=group_id)
        excursionist = EXCURSIONIST.objects.get(USER_ID_id=user_id)
        if not group.excursionist.contains(excursionist):
            group.excursionist.add(excursionist)
        else:
            return HttpResponse("Already exists")
        return HttpResponse('OK')


class CheckgroupView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GroupSerializer

    def get_queryset(self):
        user, _ = JWTAuthentication().authenticate(self.request)
        if not user.is_authenticated:
            return None
        return GROUP.objects.get_queryset().filter(excursionist__USER_ID_id=user)


def stub_add_status(request):
    return add_status_or_accreditation(request)


def get_page_object(information_list: QuerySet, size: int, page_number: int):
    # Делим полученные данные на страницы
    paginator = Paginator(information_list, size)

    # Манипуляция с номером страницы
    if page_number < 1:
        page_number *= -1
        page_number %= paginator.num_pages
        page_number = paginator.num_pages - page_number
    if page_number > paginator.num_pages:
        page_number %= paginator.num_pages
        if page_number == 0:
            page_number = paginator.num_pages

    return paginator.get_page(page_number)


def message_email(msg_subject: str, body: str):
    mail = "hrkfyr231g12f@mail.ru"
    password = "PZ81ZVpQT8J1b5set7EQ"

    msg = MIMEMultipart()
    msg['From'] = mail
    msg['To'] = mail
    msg['Subject'] = msg_subject  # Тема сообщения
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.mail.ru', 587)
    server.starttls()
    server.login(mail, password)
    server.send_message(msg)
    server.quit()
    return "OK"


def add_status_or_accreditation(request):
    institution = request.GET.get("institution")
    name = request.GET.get("name")
    date_issue = request.GET.get("date_issue")
    date_cancellation = request.GET.get("date_cancellation")
    if institution is None or name is None \
            or date_issue is None or date_cancellation is None:
        return HttpResponseBadRequest("<h2>BROKEN DATA</h2>")

    msg_subject = 'Хочу захватить Казахстан cо статусом инвалида'
    body = "institution: " + str(institution) + "\n" + \
           "name" + str(name) + "\n" + \
           "date_issue: " + str(date_issue) + "\n" + \
           "date_cancellation: " + str(date_cancellation) + "\n"

    status = message_email(msg_subject, body)

    return HttpResponse(status)
