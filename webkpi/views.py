from django.shortcuts import render
from .models import Position, Department, Employee


def positions(req):
    posits = Position.objects.all()
    if req.user.is_authenticated:
        name = 'Hello, ' + req.user.first_name + ' ' + req.user.last_name
    else:
        name = 'Anonymous'
    return render(req, './positions.html', {'positions': posits, 'name': name})


def departments(req):
    depts = Department.objects.all()
    return render(req, './departments.html', {'departments': depts})


def employees(req):
    empls = Employee.objects.all()
    return render(req, './employees.html', {'employees': empls})


def register(req):
    

def register_user(req):

