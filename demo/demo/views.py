# -*- coding: utf-8 -*-

from random import choice

from functools import wraps

from django.http import HttpResponse


def dec_wraps(func):
    @wraps(func)
    def tmp(request, *args, **kwargs):
        return func(request, *args, **kwargs)

    return tmp


def home(request):
    range(choice(range(10000000)))
    return HttpResponse('OK')


@dec_wraps
def dec(request):
    return HttpResponse('OK')
