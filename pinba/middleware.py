# -*- coding: utf-8 -*-

from pinba.defaults import PINBA_SERVER, PINBA_PORT, PINBA_ENABLED
from pinba.monitor import Monitor


if PINBA_ENABLED:
    monitor = Monitor((PINBA_SERVER, PINBA_PORT))


class PinbaMiddleware(object):
    def process_request(self, request):
        if PINBA_ENABLED:
            monitor.start(request)

    def process_response(self, request, response):
        if PINBA_ENABLED:
            return monitor.stop(response)
        return response
