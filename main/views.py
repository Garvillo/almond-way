# -*- coding: utf-8 -*--

from django.shortcuts import render
from django.shortcuts import redirect

def home(request):
    if request.user.is_authenticated:
       return render(request, 'home.html', {})

    else:
        return redirect('login')

