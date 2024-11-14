from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EmployeeForm
from .models import Employee
from django.contrib.auth import (
    authenticate,
    login as auth_login,
    logout as auth_logout,
)


# Create your views here.


@login_required
def home(request):
    employee_count = Employee.objects.count()
    department_count = 28  # Static value
    project_count = 10  # Static value

    male_count = Employee.objects.filter(gender="Male").count()
    female_count = Employee.objects.filter(gender="Female").count()
    junior_count = Employee.objects.filter(job_level="Junior").count()
    mid_level_count = Employee.objects.filter(job_level="Mid-Level").count()
    senior_count = Employee.objects.filter(job_level="Senior").count()
    head_count = Employee.objects.filter(job_level="Head").count()

    department_counts = [
        Employee.objects.filter(department=dept[0]).count()
        for dept in Employee.DEPARTMENT_CHOICES
    ]

    context = {
        "employee_count": employee_count,
        "department_count": department_count,
        "project_count": project_count,
        "male_count": male_count,
        "female_count": female_count,
        "junior_count": junior_count,
        "mid_level_count": mid_level_count,
        "senior_count": senior_count,
        "head_count": head_count,
        "department_counts": department_counts,
    }
    return render(request, "Employee/dashboard.html", context)


def custom_login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            auth_login(request, user)
            next_url = request.GET.get("next", "home")
            return redirect(next_url)
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "Employee/login.html")


def custom_logout_view(request):
    auth_logout(request)
    return redirect("login")


@login_required
def create_view(request):
    employee_form = EmployeeForm()
    if request.method == "POST":
        employee_form = EmployeeForm(request.POST, request.FILES)
        if employee_form.is_valid():
            employee_data = {
                "first_name": employee_form.cleaned_data["first_name"],
                "last_name": employee_form.cleaned_data["last_name"],
                "middle_name": employee_form.cleaned_data["middle_name"],
                "date_of_birth": employee_form.cleaned_data["date_of_birth"],
                "gender": employee_form.cleaned_data["gender"],
                "email": employee_form.cleaned_data["email"],
            }
            if Employee.objects.filter(**employee_data).exists():
                messages.error(
                    request, "An Employee with these credentials already exists"
                )
            else:
                employee_form.save()
                return redirect("employee_list")
    content = {"employee_form": employee_form}
    return render(request, "Employee/employee_create.html", content)


@login_required
def read_view(request):
    employees = Employee.objects.all()
    content = {"employees": employees}
    return render(request, "Employee/employee_list.html", content)


@login_required
def profile_view(request, employee_id):
    profiles = Employee.objects.get(employee_id=employee_id)
    content = {"profiles": profiles}
    return render(request, "Employee/employee_profile.html", content)


@login_required
def update_view(request, employee_id):
    employee = Employee.objects.get(employee_id=employee_id)
    employee_form = EmployeeForm(instance=employee)
    if request.method == "POST":
        employee_form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if employee_form.is_valid():
            employee_data = {
                "first_name": employee_form.cleaned_data["first_name"],
                "last_name": employee_form.cleaned_data["last_name"],
                "middle_name": employee_form.cleaned_data["middle_name"],
                "date_of_birth": employee_form.cleaned_data["date_of_birth"],
                "gender": employee_form.cleaned_data["gender"],
                "email": employee_form.cleaned_data["email"],
            }
            if Employee.objects.filter(**employee_data).exists():
                messages.error(
                    request, "An Employee with these credentials already exists"
                )
            else:
                employee_form.save()
                return redirect("employee_list")
    content = {"employee_form": employee_form}
    return render(request, "Employee/employee_update.html", content)


def delete_view(request, employee_id):
    employee = Employee.objects.get(employee_id=employee_id)
    employee.delete()
    return redirect("employee_list")
