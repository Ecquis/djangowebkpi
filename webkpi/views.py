from django.shortcuts import render
from .models import Position, Department, Employee


def positions(req):
    posits = Position.objects.all()
    return render(req, './positions.html', {'positions': posits})


def departments(req):
    depts = Department.objects.all()
    return render(req, './departments.html', {'departments': depts})


def employees(req):
    empls = Employee.objects.all()
    return render(req, './employees.html', {'employees': empls})
