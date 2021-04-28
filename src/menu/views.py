from django.shortcuts import render
from collections import defaultdict

from .models import Screen


def screen_viewer(request, screen_id):
    screen = Screen.objects.get(pk=screen_id)

    columns = defaultdict(list)
    layouts = screen.category_layouts.all()
    for layout in layouts:
        columns[layout.column].append(layout.category)
    context = {"screen": screen, "columns": {**columns}}
    return render(request, "menu/screen_viewer.html", context)


def index(request):
    screens = Screen.objects.all()
    context = {"screens": screens}
    return render(request, "menu/index.html", context)
