from django.shortcuts import render, redirect
from .models import Employee, Company,Delegation, Device
from .forms import EmployeeForm, DelegationForm
from django.utils import timezone

# Create your views here.


# The views to handle employee-related actions for each company

def company_dashboard(request, company_id):
    company = Company.objects.get(pk=company_id)
    employees = company.employee_set.all()
    return render(request, 'company_dashboard.html', {'company': company, 'employees': employees})

def add_employee(request, company_id):
    company = Company.objects.get(pk=company_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.company = company
            employee.save()
            return redirect('company_dashboard', company_id=company_id)
    else:
        form = EmployeeForm()
    return render(request, 'add_employee.html', {'form': form, 'company': company})

def update_employee(request, company_id, employee_id):
    company = Company.objects.get(pk=company_id)
    employee = Employee.objects.get(pk=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('company_dashboard', company_id=company_id)
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'update_employee.html', {'form': form, 'company': company, 'employee': employee})

def delete_employee(request, company_id, employee_id):
    company = Company.objects.get(pk=company_id)
    employee = Employee.objects.get(pk=employee_id)
    if request.method == 'POST':
        employee.delete()
        return redirect('company_dashboard', company_id=company_id)
    return render(request, 'delete_employee.html', {'company': company, 'employee': employee})



#  the views to handle device delegation transactions
def delegate_device(request, company_id):
    company = Company.objects.get(pk=company_id)
    if request.method == 'POST':
        form = DelegationForm(request.POST)
        if form.is_valid():
            delegation = form.save(commit=False)
            delegation.save()
            return redirect('company_dashboard', company_id=company_id)
    else:
        form = DelegationForm()
    return render(request, 'delegate_device.html', {'form': form, 'company': company})

def undelegate_device(request, company_id, delegation_id):
    company = Company.objects.get(pk=company_id)
    delegation = Delegation.objects.get(pk=delegation_id)
    if request.method == 'POST':
        delegation.delete()
        return redirect('company_dashboard', company_id=company_id)
    return render(request, 'undelegate_device.html', {'company': company, 'delegation': delegation})




# the views to display the device delegation history
def device_history(request, device_id):
    device = Device.objects.get(pk=device_id)
    history = Delegation.objects.filter(device=device).order_by('-check_out_date')
    return render(request, 'device_history.html', {'device': device, 'history': history})



def device_list(request):
    devices = Device.objects.all()
    return render(request, 'device_list.html', {'devices': devices})


"""""
def assign_asset(request, asset_id):
    asset = Asset.objects.get(pk=asset_id)
    if request.method == 'POST':
        employee_id = request.POST['employee']
        assigned_to = Employee.objects.get(pk=employee_id)
        asset.assigned_to = assigned_to
        asset.assigned_date = timezone.now().date()
        asset.save()
        return redirect('asset_list')
    employees = Employee.objects.all()
    return render(request, 'assign_asset.html', {'asset': asset, 'employees': employees})

def return_asset(request, asset_id):
    asset = Asset.objects.get(pk=asset_id)
    if request.method == 'POST':
        asset.assigned_to = None
        asset.return_date = timezone.now().date()
        asset.save()
        return redirect('asset_list')
    return render(request, 'return_asset.html', {'asset': asset})

"""
