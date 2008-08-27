from django import template
from django.contrib.auth.models import AnonymousUser, User

from codereview import library
from gae2django.utils import CallableString


def nickname(email, arg=None):
    if isinstance(email, AnonymousUser):
        email = None
    elif isinstance(email, User):
        email.email = CallableString(email.email)
    return library.nickname(email, arg)


def show_user(email, arg=None, autoescape=None, memcache_results=None):
    if isinstance(email, AnonymousUser):
        email = None
    elif isinstance(email, User):
        email.email = CallableString(email.email)
    return library.show_user(email, arg, autoescape, memcache_results)


# Make filters global
template.defaultfilters.register.filter('nickname', nickname)
template.defaultfilters.register.filter('show_user', show_user)