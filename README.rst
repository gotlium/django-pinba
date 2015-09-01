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

    $  pip install django-pinba


2. Add ``pinba.middleware.PinbaMiddleware`` middleware to ``MIDDLEWARE_CLASSES`` on your settings

3. Add pinba-engine server configuration:

.. code-block:: python

    PINBA_SERVER = '192.168.55.11'
    PINBA_PORT = 30002
    PINBA_ENABLED = True
    PINBA_DISABLE_ADMIN = True


Timers
------
.. code-block:: python

    from time import sleep
    from pinba.timers import get_monitor

    monitor = get_monitor()
    timer = monitor.timer(foo='bar')
    timer.start()
    sleep(0.5)
    timer.stop()
    monitor.send()


Requirements
------------
* PinbaEngine==1.1.0
* PinBoard==1.5.2
* pynba==0.5.4


Credits
-------

- PinbaEngine_
- Pynba_
- PinBoard_

.. _PinbaEngine: http://pinba.org
.. _Pynba: https://github.com/johnnoone/pynba
.. _PinBoard: https://github.com/intaro/pinboard


.. image:: https://d2weczhvl823v0.cloudfront.net/gotlium/django-pinba/trend.png
    :alt: Bitdeli badge
    :target: https://bitdeli.com/free
