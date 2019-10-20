from django.shortcuts import render
from django.shortcuts import redirect
from .models import Position, Department, Employee


def check_user(user):
    if user.is_authenticated:
        return user.first_name + ' ' + user.last_name
    else:
        return 'Anonymous'


def positions(req):
    posits = Position.objects.all()
    name = check_user(req.user)
    return render(req, './positions.html', {'positions': posits, 'name': name})


def departments(req):
    depts = Department.objects.all()
    name = check_user(req.user)
    return render(req, './departments.html', {'departments': depts, 'name': name})


def employees(req):
    empls = Employee.objects.all()
    name = check_user(req.user)
    return render(req, './employees.html', {'employees': empls, 'name': name})


def form_employees(req):
    depts = Department.objects.all()
    posits = Position.objects.all()
    name = check_user(req.user)
    return render(req, './add_employee.html', {'departments': depts, 'positions': posits, 'name': name})


def form_department(req):
    return render(req, './add_department.html', {})


def form_positions(req):
    return render(req, './add_position.html', {})


def add_position(req):
    if req.POST:
        new_pos = Position()
        new_pos.title = req.POST['name']

        new_pos.save()

    return redirect("/positions")


def add_department(req):
    if req.POST:
        new_dep = Department()
        new_dep.title = req.POST['name']
        new_dep.city = req.POST['city']
        new_dep.phone = req.POST['phone']
        new_dep.address = req.POST['address']

        new_dep.save()

    return redirect("/departments")


def add_employee(req):
    if req.POST:
        print(req.POST)
        new_emp = Employee()
        new_emp.first_name = req.POST['firstname']
        new_emp.last_name = req.POST['lastname']
        new_emp.date_birth = req.POST['birth']
        new_emp.date_employment = req.POST['employed']
        new_emp.phone = req.POST['phone']
        new_emp.position = Position.objects.get(id__exact = int(req.POST['postId']))
        new_emp.department = Department.objects.get(id__exact = int(req.POST['departmentId']))

        new_emp.save()

    return redirect("/employees")
