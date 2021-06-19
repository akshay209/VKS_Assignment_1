from django.shortcuts import render
import numpy as np
from string import ascii_letters

from django.views.generic import TemplateView


class MainPage(TemplateView):
    template_name = 'home.html'

global mat

def mainpage(request):
    row = int(request.POST['Row'])
    col = int(request.POST['Column'])
    ll = int(request.POST['Lower_limit'])
    ul = int(request.POST['Upper_limit'])
    mat = np.random.randint(ll, ul + 1, size=(row, col))
    # print(mat)
    tra = np.transpose(mat)
    # ss = '\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in mat])
    return render(request, "home.html", {"mat": mat, "tra":tra})

