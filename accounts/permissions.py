from django.http import HttpResponse
from django.shortcuts import redirect


def checking_login(func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return func(request, *args, **kwargs)
    return wrapper

def checking_admin(func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.role != 'admin':
                return HttpResponse('Access denied!')
        return func(request, *args, **kwargs)
    return wrapper