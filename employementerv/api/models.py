from django.db import models

# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    department=models.CharField(max_length=200)
    salary=models.PositiveIntegerField()
    age=models.PositiveIntegerField()
    contact=models.CharField(max_length=200,null=True)

    @property
    def tasks(self):
        qs=Task.objects.filter(employees=self)
        return qs

    def __str__(self):
        return self.name

class Task(models.Model):
    name=models.CharField(max_length=200)
    employees=models.ForeignKey(Employee,on_delete=models.CASCADE)
    options=(
        ("pending","pending"),
        ("inprogress","inprogress"),
        ("completed","completed")
    )
    status=models.CharField(max_length=200,choices=options,default="pending")
    assg_date=models.DateTimeField(auto_now=True)
    due_date=models.DateField(null=True)

    def __str__(self):
        return self.name