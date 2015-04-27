# -*- coding: utf-8 -*-
"""
    IsCool-e Pynba
    ~~~~~~~~~~~~~~

    :copyright: (c) 2012 by IsCool Entertainment.
    :license: MIT, see LICENSE for more details.
"""

import logging
import socket
from pinba.message import dumps

logger = logging.getLogger('pinba')


class Reporter(object):
    def __init__(self, address, raise_on_fail=False):
        self.address = address
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.raise_on_fail = raise_on_fail

    def __call__(self, server_name, hostname, script_name,
                 elapsed, ru_utime=0.0, ru_stime=0.0,
                 document_size=0, memory_peak=0, status=200,
                 memory_footprint=0, schema='http'):

        self.send(dumps(**{
            'hostname': hostname,
            'server_name': server_name,
            'script_name': script_name,
            'request_count': 1,
            'document_size': document_size,
            'memory_peak': memory_peak,
            'request_time': elapsed,
            'ru_utime': ru_utime,
            'ru_stime': ru_stime,
            'status': status,
            'memory_footprint': memory_footprint,
            'schema': schema,
        }))

    def send(self, msg):
        try:
            return self.sock.sendto(msg, self.address)
        except Exception as error:
            if self.raise_on_fail:
                raise
            logger.exception(error)
        return None
