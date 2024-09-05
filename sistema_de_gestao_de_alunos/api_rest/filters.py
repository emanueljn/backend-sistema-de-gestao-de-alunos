from dj_rql.filter_cls import AutoRQLFilterClass
from django.contrib.auth.models import User
class UserFilterClass(AutoRQLFilterClass):
    MODEL = User