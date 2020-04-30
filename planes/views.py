from django.shortcuts import render, HttpResponse, redirect

'''Autorization and auntification'''
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_protect # https://docs.djangoproject.com/en/3.0/ref/csrf/


# Create your views here.

@csrf_protect
def login(request):
    template_name = 'login/login.html'
    context = {}
    if request.user.is_authenticated:
        return HttpResponse('redirect somewhere')
        # return redirect()
    if request.method == 'POST':
        password = request.POST['password']
        login = request.POST['login']
        user = auth.authenticate(username=login, password=password)
        if user:
            auth.login(request, user)
            return HttpResponse('Залогинено успешно')
            # return redirect()
        else:
            err_text = 'Неверный Email/Пароль'
            context['error'] = err_text
            return render(request, template_name, context)
    return render(request, template_name, context)
