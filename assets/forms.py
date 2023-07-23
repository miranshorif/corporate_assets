from django import forms
from .models import Employee, Delegation, Device

#define a form for adding employees

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'email']
        
        
        
#define a form for the device delegation transaction
class DelegationForm(forms.ModelForm):
    class Meta:
        model = Delegation
        fields = ['device', 'assigned_to', 'start_date', 'end_date', 'condition_on_check_out', 'condition_on_return']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        company = kwargs.get('instance').assigned_to.company if 'instance' in kwargs else None
        if company:
            self.fields['device'].queryset = Device.objects.filter(delegation__isnull=True)