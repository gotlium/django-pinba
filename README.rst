Django-Pinba
============

What's that
-----------
App for collect Django statistics into PinbaEngine.


Publications
-----------
* `Completely installation and usage on production <http://habrahabr.ru/post/200128/>`_.


Quick installation
------------------
1. Using pip:

.. code-block:: bash

    $  sudo pip install django-pinba


2. Add ``pinba.middleware.PinbaMiddleware`` middleware to ``MIDDLEWARE_CLASSES`` on your settings

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
