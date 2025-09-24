from django.conf import settings
from django.utils.module_loading import import_string

def get_delivery_callback():
    path = getattr(settings, "AWS_DJANGO_SES_DELIVERY_CALLBACK", None)
    if path is None:
        return None
    return import_string(path)
