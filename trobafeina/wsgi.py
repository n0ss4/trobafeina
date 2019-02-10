"""
WSGI config for trobafeina project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/home/trobafeina/venv/lib/python2.7/site-packages')

INTERP = os.path.expanduser("~/venv/bin/python")

if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

sys.path.insert(0,'$HOME/venv/bin')
sys.path.insert(0,'$HOME/venv/lib/python2.7/site-packages/django')
sys.path.insert(0,'$HOME/venv/lib/python2.7/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('/home/trobafeina/trobafeina/trobafeina')

os.environ['DJANGO_SETTINGS_MODULE'] = 'trobafeina.settings'

# Activate your virtual env
activate_env=os.path.expanduser("/home/trobafeina/venv/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

"""from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()"""
