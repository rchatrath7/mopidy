"""
Frontend which lets you control Mopidy through HTTP and WebSockets.

**Dependencies**

- ``cherrypy``

- ``ws4py``

**Settings**

- :attr:`mopidy.settings.HTTP_SERVER_HOSTNAME`

- :attr:`mopidy.settings.HTTP_SERVER_PORT`

- :attr:`mopidy.settings.HTTP_SERVER_STATIC_DIR`

**Usage**

When this frontend is included in :attr:`mopidy.settings.FRONTENDS`, it starts
a web server at the port specified by :attr:`mopidy.settings.HTTP_SERVER_PORT`.

This web server exposes a WebSocket at ``/ws``. The WebSocket gives you access
to Mopidy's full API and enables Mopidy to instantly push events to the client,
as they happen.

The web server can also host any static files, for example the HTML, CSS,
JavaScript and images needed by a web based Mopidy client. To host static
files, change :attr:`mopidy.settings.HTTP_SERVER_STATIC_DIR` to point to the
directory you want to serve.

**API stability**

This frontend is currently to be regarded as **experimental**, and we are not
promising to keep any form of backwards compatibility between releases.
"""

# flake8: noqa
from .actor import HttpFrontend
