from django.db import models

class StaffBase(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    class Meta:
        abstract = True

    def get_role(self):
        return "Staff"

class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

class Manager(StaffBase):
    department = models.CharField(max_length=100)
    has_company_card = models.BooleanField(default=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)

    def get_role(self):
        return "Manager"

class Intern(StaffBase):
    mentor = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True)
    internship_end = models.DateField()
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)

    def get_role(self):
        return "Intern"
