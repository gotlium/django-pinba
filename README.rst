Django-Pinba
============

What's that
-----------
App for collect Django statistics into PinbaEngine.

Installation:
-------------
1. Package:

.. code-block:: bash

    $  sudo pip install django-pinba

2. Add the ``pinba.middleware.PinbaMiddleware`` application
    to ``MIDDLEWARE_CLASSES`` in your settings
3. Add pinba-engine server configuration:

.. code-block:: python

    PINBA_SERVER = '192.168.55.11'
    PINBA_PORT = 30002
    PINBA_ENABLED = True


Credits
-------

- Pinba_
- pynba_

.. _Pinba: http://pinba.org
.. _pynba: https://pypi.python.org/pypi/iscool_e.pynba
