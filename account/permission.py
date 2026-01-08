from django.core.exceptions import PermissionDenied
from django.http import HttpResponse


def required_user(func,*args,**kwargs):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied()

        return func(request,*args,**kwargs)
    return wrapper


def admin_required(func):
    def wrapper(request,*args,**kwargs):
        if  request.user.is_authenticated and request.user.role=='admin':
            return func(request, *args, **kwargs)
        else:
            return HttpResponse("Siz admin emassiz")



    return wrapper
