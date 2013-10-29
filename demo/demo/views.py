# -*- coding: utf-8 -*-


from django.http import HttpResponse
from random import choice
from django.contrib.auth.models import User

def home(request):
    a = range(choice(range(10000000)))
    User.objects.get(pk=1)
    return HttpResponse('OK')