# -*- coding: utf-8 -*-

from random import choice
from time import sleep
from functools import wraps

from django.http import HttpResponse

from pinba.timers import get_monitor


def dec_wraps(func):
    @wraps(func)
    def tmp(request, *args, **kwargs):
        return func(request, *args, **kwargs)

    return tmp


def home(request):
    range(choice(range(10000000)))
    return HttpResponse('OK\n')


@dec_wraps
def dec(request):
    return HttpResponse('OK\n')


def timer_view(request):
    monitor = get_monitor()
    timer = monitor.timer(foo='bar')
    timer.start()
    sleep(0.5)
    timer.stop()
    monitor.send()
    return HttpResponse('OK\n')
