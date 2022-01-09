import smtplib

# Добавляем необходимые подклассы - MIME-типы
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.contrib.auth.models import User
from django.db.models import QuerySet
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, HttpResponsePermanentRedirect

# Create your views here.

# Общие функции(без логина)
from db_course_work_backend.models import EXHIBITION, GROUP, PERSONAL_DATA, PLACE, EXHIBIT, MUSEUM, PASSPORT, GUIDE, \
    EXCURSIONIST, EXCURSION, DOCUMENT_STATUS, DOCUMENT_ACCREDITATION


def view_list_excursions(request):
    # Получаем данные
    size = request.GET.get("size", 15)
    page_number = request.GET.get("page", 1)

    # Получаем данные и проверяем на существование
    exhibition_list = EXHIBITION.objects.get_queryset().order_by('id')
    if not exhibition_list.exists():
        return HttpResponseNotFound("<h2>Not Found EXHIBIT</h2>")

    # Получение определенной страницы с данными
    page_obj = get_page_object(exhibition_list, size, page_number)

    return HttpResponse(page_obj)


def view_list_groups_tour(request):
    # Получаем данные
    size = request.GET.get("size", 15)
    page_number = request.GET.get("page", 1)
    excursions_id = request.GET.get("excursions_id", 1)

    # Получаем данные и проверяем на существование
    group_list = GROUP.objects.get_queryset().filter(EXHIBITION_ID=excursions_id).order_by('id')
    if not group_list.exists():
        return HttpResponseNotFound("<h2>Not Found GROUP</h2>")

    # Получение определенной страницы с данными
    page_obj = get_page_object(group_list, size, page_number)

    return HttpResponse(page_obj)


def become_guide(request):
    # Получаем данные
    mobile_number = request.POST.get("mobile_number")
    email_guide = request.POST.get("email")
    series_passport = request.POST.get("series_passport")
    number_passport = request.POST.get("number_passport")
    surname = request.POST.get("surname")
    name = request.POST.get("name")
    patronymic = request.POST.get("patronymic")
    gender = request.POST.get("gender")
    date_birthday = request.POST.get("date_birthday")
    passport_issue = request.POST.get("passport_issue")
    date_issue = request.POST.get("date_issue")

    # Проверяем заполненность полей
    if mobile_number is None or series_passport is None \
            or number_passport is None or surname is None \
            or name is None or patronymic is None or gender is None \
            or date_birthday is None or passport_issue is None or date_issue is None:
        return HttpResponseNotFound("<h2>BROKEN DATA</h2>")

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


def register_become_random_dick(request):
    # Получаем данные
    username = request.POST.get("username")
    password = request.POST.get("password")

    new_user = User.objects.create(username='new_user')
    new_user.set_password('password')
    return HttpResponse('Голые телки и мужики')


# Гид функции
def stub_add_accreditation(request):
    return add_status_or_accreditation(request)


# Рандом хуй функции
def add_to_group(request):
    return HttpResponse('Голые телки и мужики')


def stub_add_status(request):
    return add_status_or_accreditation(request)


def default_page(request):
    return HttpResponsePermanentRedirect("/excursions")


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
        return HttpResponseNotFound("<h2>BROKEN DATA</h2>")

    msg_subject = 'Хочу захватить Казахстан cо статусом инвалида'
    body = "institution: " + str(institution) + "\n" + \
           "name" + str(name) + "\n" + \
           "date_issue: " + str(date_issue) + "\n" + \
           "date_cancellation: " + str(date_cancellation) + "\n"

    status = message_email(msg_subject, body)

    return HttpResponse(status)
