from django.db import models


class Department(models.Model):
    # id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Position(models.Model):
    # id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Employee(models.Model):
    # id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_birth = models.DateField()
    date_employment = models.DateField()
    phone = models.CharField(max_length=30)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
