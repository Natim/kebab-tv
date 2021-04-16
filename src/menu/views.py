from django.shortcuts import render

from .models import Screen


def screen_viewer(request, screen_id):
    screen = Screen.objects.get(screen_id)
    context = {'screen': screen}
    return render(request, 'menu/screen_viewer.html', context)

def index(request):
    screens = Screen.objects.all()
    context = {'screens': screens}
    return render(request, 'menu/index.html', context)
