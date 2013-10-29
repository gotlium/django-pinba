# -*- coding: utf-8 -*-

import resource
import socket
import time

from django.core.urlresolvers import resolve

from iscool_e.pynba.reporter import Reporter


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

    def start(self, request):
        self.resources = resource.getrusage(resource.RUSAGE_SELF)
        self.start_time = time.time()
        self.request = request

    def stop(self, response):
        self.usage = resource.getrusage(resource.RUSAGE_SELF)
        self.elapsed = (time.time() - self.start_time)
        self.response = response

        self._calculate()
        self._send()
        return response

    def _calculate(self):
        self.ru_utime = self.usage.ru_utime - self.resources.ru_utime
        self.ru_stime = self.usage.ru_stime - self.resources.ru_stime
        self.server_name = self.request.META.get('SERVER_NAME')
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

    def _send(self):
        self.reporter(
            document_size=self.document_size,
            memory_peak=self.memory_peak,
            servername=self.server_name,
            scriptname=self.script_name,
            hostname=self.hostname,
            ru_utime=self.ru_utime,
            ru_stime=self.ru_stime,
            elapsed=self.elapsed,
            timers=[],
            status=self.status,
        )
