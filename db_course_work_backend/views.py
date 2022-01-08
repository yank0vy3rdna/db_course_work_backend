from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound

# Общие функции(без логина)
from db_course_work_backend.models import EXHIBITION


def view_list_excursions(request):
    output = EXHIBITION.objects.all()
    if not output.exists():
        return HttpResponseNotFound("<h2>Not Found EXHIBIT</h2>")
    return HttpResponse(output)


def view_list_groups_tour(request):
    return HttpResponse('Голые телки и мужики')


def stub_become_guide(request):
    return HttpResponse('Голые телки и мужики')


def register_become_random_dick(request):
    return HttpResponse('Голые телки и мужики')


# Общие функции(с логином)
def see_list_dudes_from_group(request):
    return HttpResponse('Голые телки и мужики')


# Гид функции
def create_groups(request):
    return HttpResponse('Голые телки и мужики')


def excursions(request):
    return HttpResponse('Голые телки и мужики')


def stub_add_accreditation(request):
    return HttpResponse('Голые телки и мужики')


# Рандом хуй функции
def add_to_group(request):
    return HttpResponse('Голые телки и мужики')


def stub_add_status(request):
    return HttpResponse('Голые телки и мужики')
