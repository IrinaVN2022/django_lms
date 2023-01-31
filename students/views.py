from urllib import response

#import args
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from webargs.fields import Str
from webargs.djangoparser import use_args

from .models import Student
from .util import format_list_student


# HttpRequest
# HttpResponse


def view_with_param(request, value):
    return HttpResponse(f'With param: "{value}"')


def view_without_param(request):
    return HttpResponse('Without param')


def index(request):
    return HttpResponse('Welcome to lms')


'''@use_args(
    {
        'first_name': Str(required=False),
        'last_name': Str(required=False),
    },
    location='query',
)'''
'''def get_students(request):
    students = Student.objects.all().order_by('birthday')
    if 'first_name' in args:
        students = students.filter(first_name=args['first_name'])
    if 'last_name' in args:
        students = students.filter(first_name=args['last_name'])

    string = format_list_student(students)
    response = HttpResponse(string)
    return response'''
