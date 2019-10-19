from django.db import models
state_list = ((0, 'Gujarat'),(1, 'Maharashtra'),( 2, 'Punjab'))
department_list = ((0, 'IT-Department'),( 1, 'HR-Department'))


class Employee(models.Model):
    eid = models.CharField(max_length=20)
    ename = models.CharField(max_length=100)
    eemail = models.EmailField()
    econtact = models.CharField(max_length=15)
    edescription = models.CharField(max_length=50, null=True, blank=True)
    state = models.IntegerField(choices=state_list)

    def __str__(self):
        return self.ename

class Department(models.Model):
    department = models.ForeignKey(Employee, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name