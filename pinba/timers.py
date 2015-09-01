# -*- encoding: utf-8 -*-

import inspect
from pynba.util import ScriptMonitor

from pinba.defaults import PINBA_SERVER, PINBA_PORT, PINBA_SERVER_NAME


def get_monitor(host=PINBA_SERVER, port=PINBA_PORT, *args, **kwargs):
    """
    todo: memory + cpu
    """
    kwargs['servername'] = PINBA_SERVER_NAME
    kwargs['scriptname'] = __file__

    for item in inspect.stack():
        if item and __file__ not in item:
            kwargs['scriptname'] = item[3]
            break

    return ScriptMonitor((host, port), *args, **kwargs)
