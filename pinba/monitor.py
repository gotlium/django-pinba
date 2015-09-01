# -*- coding: utf-8 -*-

import resource
import socket
import time
import os

from django.core.urlresolvers import resolve

from pynba.core.reporter import Reporter
from pinba import defaults


now = time.clock if os.name == 'nt' else time.time


class Monitor(object):
    def __init__(self, address):
        self.hostname = socket.gethostname()
        self.reporter = Reporter(address)
        self.document_size = None
        self.memory_peak = None
        self.script_name = None
        self.server_name = None
        self.start_time = None
        self.resources = None
        self.ru_utime = None
        self.ru_stime = None
        self.response = None
        self.request = None
        self.elapsed = None
        self.usage = None
        self.status = 200

    def get_server_name(self):
        if defaults.PINBA_SERVER_NAME is not None:
            return defaults.PINBA_SERVER_NAME
        return self.request.META.get('SERVER_NAME')

    def start(self, request):
        self.resources = resource.getrusage(resource.RUSAGE_SELF)
        self.start_time = now()
        self.request = request

    def stop(self, response):
        self.usage = resource.getrusage(resource.RUSAGE_SELF)
        self.elapsed = (now() - self.start_time)
        self.response = response

        self._calculate()
        self._send()
        return response

    def _calculate(self):
        self.ru_utime = self.usage.ru_utime - self.resources.ru_utime
        self.ru_stime = self.usage.ru_stime - self.resources.ru_stime
        self.server_name = self.get_server_name()
        self.document_size = len(self.response.content)
        self.script_name = self._get_script_name()
        self.memory_peak = self.usage.ru_maxrss
        self.status = self.response.status_code

    def _get_script_name(self):
        try:
            current_view = resolve(self.request.path)[0]
            return '%s.%s' % (current_view.__module__, current_view.__name__)
        except:
            return self.request.path

    def _get_scheme(self):
        if hasattr(self.request, 'scheme'):
            return self.request.scheme
        return 'http'

    def _send(self):
        self.reporter(
            self.server_name,
            self.hostname,
            self.script_name,
            self.elapsed,
            timers=None,
            document_size=self.document_size,
            memory_peak=self.memory_peak,
            ru_utime=self.ru_utime,
            ru_stime=self.ru_stime,
            status=self.status,
            schema=self._get_scheme(),
            # memory_footprint=self.memory_peak,
        )
