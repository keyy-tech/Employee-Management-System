from .models import Employee
from django import forms
from django.core.exceptions import ValidationError


def validate_phone_number(value):
    if len(value) != 10 or not value.isdigit():
        raise ValidationError("Phone number must be exactly 10 digits.")


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        exclude = ["employee_id"]
        labels = {
            # Basic Information
            "first_name": "First Name",
            "last_name": "Last Name",
            "middle_name": "Middle Name",
            "date_of_birth": "Date of Birth",
            "gender": "Gender",
            "nationality": "Nationality",
            "marital_status": "Marital Status",
            # Contact Information
            "email": "Email",
            "phone_number": "Phone Number",
            "address": "Address",
            "city": "City",
            "state": "State",
            "postal_code": "Postal Code",
            "country": "Country",
            # Job Details
            "job_level": "Job Level",
            "job_title": "Job Title",
            "employment_type": "Employment Type",
            "job_position": "Job Position",
            "date_of_hire": "Date of Hire",
            "date_of_termination": "Date of Termination",
            "department": "Department",
            # Salary Information
            "salary": "Salary",
            "pay_frequency": "Pay Frequency",
            "bank_account_number": "Bank Account Number",
            "bank_name": "Bank Name",
            "bank_branch": "Bank Branch",
            # Emergency Contact Information
            "emergency_contact_name": "Emergency Contact Name",
            "emergency_contact_relationship": "Emergency Contact Relationship",
            "emergency_contact_phone": "Emergency Contact Phone",
            "emergency_contact_address": "Emergency Contact Address",
            # Employment Status & History
            "status": "Status",
            "previous_positions": "Previous Positions",
            # Additional Information
            "profile_picture": "Profile Picture",
        }
        widgets = {
            "first_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter first name"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter last name"}
            ),
            "middle_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter middle name"}
            ),
            "date_of_birth": forms.DateInput(
                attrs={"class": "form-control", "placeholder": "Enter date of birth"},
                format="%Y-%m-%d",
            ),
            "gender": forms.Select(attrs={"class": "form-control"}),
            "nationality": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter nationality"}
            ),
            "marital_status": forms.Select(attrs={"class": "form-control"}),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Enter email"}
            ),
            "phone_number": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter phone number"}
            ),
            "address": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter address"}
            ),
            "city": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter city"}
            ),
            "state": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter state"}
            ),
            "postal_code": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter postal code"}
            ),
            "country": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter country"}
            ),
            "job_level": forms.Select(attrs={"class": "form-control"}),
            "job_title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter job title"}
            ),
            "employment_type": forms.Select(attrs={"class": "form-control"}),
            "job_position": forms.Select(attrs={"class": "form-control"}),
            "date_of_hire": forms.DateInput(
                attrs={"class": "form-control", "placeholder": "Enter date of hire"}
            ),
            "date_of_termination": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter date of termination",
                }
            ),
            "department": forms.Select(attrs={"class": "form-control"}),
            "salary": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Enter salary"}
            ),
            "pay_frequency": forms.Select(attrs={"class": "form-control"}),
            "bank_account_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter bank account number",
                }
            ),
            "bank_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter bank name"}
            ),
            "bank_branch": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter bank branch"}
            ),
            "emergency_contact_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter emergency contact name",
                }
            ),
            "emergency_contact_relationship": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter emergency contact relationship",
                }
            ),
            "emergency_contact_phone": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter emergency contact phone",
                }
            ),
            "emergency_contact_address": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter emergency contact address",
                }
            ),
            "status": forms.Select(attrs={"class": "form-control"}),
            "previous_positions": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter previous positions",
                }
            ),
            "profile_picture": forms.ClearableFileInput(
                attrs={"class": "form-control"}
            ),
        }
