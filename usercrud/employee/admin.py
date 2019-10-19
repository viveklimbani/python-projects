from django.contrib import admin

from .models import Employee, Department


class EmployeeAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Employee Name', {'fields': ['eid', 'ename']}),
        ('Employee Detail', {'fields': ['eemail', 'econtact', 'edescription', 'state']}),
        # ('Employee Department', {'fields': ['department']}),
    ]
    list_display = ('eid', 'ename', 'edescription')

admin.site.register(Employee, EmployeeAdmin)

class DepartmentInline(admin.StackedInline):
    model = Department

class DepartmentAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Employee Department', {'fields': ['name']}),
    ]
    list_display = ('name',)

admin.site.register(Department, DepartmentAdmin)