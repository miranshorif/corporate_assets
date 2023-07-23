from django.db import models

# Create your models here.

#Create Company Model

class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    contact_email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

#Create Employee Model

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    #Employee-Company Relationship:associate employees with their respective companies.
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


#Create Asset Model
""""
class Asset(models.Model):
    ASSET_TYPES = (
        ('Phone', 'Phone'),
        ('Laptop', 'Laptop'),
        ('Tablet', 'Tablet'),
        ('Other', 'Other'),
    )

    asset_type = models.CharField(max_length=10, choices=ASSET_TYPES)
    serial_number = models.CharField(max_length=100, unique=True)
    assigned_to = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.SET_NULL)
    assigned_date = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.asset_type} - {self.serial_number}"
"""
#include device delegation functionality to represent devices, delegation transactions
class Device(models.Model):
    DEVICE_TYPES = (
        ('Phone', 'Phone'),
        ('Laptop', 'Laptop'),
        ('Tablet', 'Tablet'),
        ('Other', 'Other'),
    )

    asset_type = models.CharField(max_length=10, choices=DEVICE_TYPES)
    serial_number = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.asset_type} - {self.serial_number}"
    
    
#represent the delegation transactions between the company and its employees

class Delegation(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    check_out_date = models.DateTimeField(auto_now_add=True)  # Timestamp for check-out
    return_date = models.DateTimeField(null=True, blank=True)  # Timestamp for return
    condition_on_check_out = models.CharField(max_length=100)
    condition_on_return = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.device} - Assigned to: {self.assigned_to}, Start Date: {self.start_date}, End Date: {self.end_date}"