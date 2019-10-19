from django.shortcuts import render
from .models import Position


def positions(req):
    pos = Position.objects.all()
    return render(req, './positions.html', {'positions': pos})
