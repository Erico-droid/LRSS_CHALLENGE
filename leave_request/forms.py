from django import forms
from .models import LeaveRequest

class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = ['user_firstname', 'user_lastname', 'start_date', 'end_date', 'leave_type']
        labels = {
            'user_firstname': 'First Name',
            'user_lastname': 'Last Name',
            'start_date': 'Start Date',
            'end_date': 'End Date',
            'leave_type': 'Type of Leave',
        }
        widgets = {
            'user_firstname': forms.TextInput(attrs={'class': 'form-control'}),
            'user_lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'leave_type': forms.Select(attrs={'class': 'form-select'}),
        }
