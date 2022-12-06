"""
The settings module inherited from config.settings is introduced for test purpose only;
this is updated with the settings only used in the following environments:
* local development
* CI
"""
import django_stubs_ext

from config.settings import *

django_stubs_ext.monkeypatch()
