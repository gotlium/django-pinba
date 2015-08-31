# -*- coding: utf-8 -*-

from django.conf import settings

PINBA_SERVER = getattr(settings, 'PINBA_SERVER', '127.0.0.1')
PINBA_PORT = getattr(settings, 'PINBA_PORT', 30002)
PINBA_ENABLED = getattr(settings, 'PINBA_ENABLED', False)
PINBA_SERVER_NAME = getattr(settings, 'PINBA_SERVER_NAME', None)
