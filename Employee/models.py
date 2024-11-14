from django.db import models
import random
import string
from django.core.exceptions import ValidationError


def validate_phone_number(value):
    if len(value) != 10 or not value.isdigit():
        raise ValidationError("Phone number must be exactly 10 digits.")


class Employee(models.Model):
    # ID
    employee_id = models.CharField(
        max_length=10, unique=True, blank=True, primary_key=True, editable=False
    )
    # Basic Information
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    date_of_birth = models.DateField()
    GENDER_CHOICES = [("Male", "Male"), ("Female", "Female")]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    nationality = models.CharField(max_length=50)
    MARITAL_CHOICES = [
        ("Single", "Single"),
        ("Married", "Married"),
        ("Divorced", "Divorced"),
        ("Widowed", "Widowed"),
    ]
    marital_status = models.CharField(max_length=10, choices=MARITAL_CHOICES)

    # Contact Information
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=10, validators=[validate_phone_number])
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50)

    # Job Details
    JOB_LEVEL_CHOICES = [
        ("Junior", "Junior"),
        ("Mid-Level", "Mid-Level"),
        ("Senior", "Senior"),
        ("Head", "Head"),
    ]
    job_level = models.CharField(
        max_length=10, choices=JOB_LEVEL_CHOICES, default="Junior"
    )
    job_title = models.CharField(max_length=100)
    EMPLOYMENT_TYPE_CHOICES = [
        ("Full-Time", "Full-Time"),
        ("Part-Time", "Part-Time"),
        ("Contract", "Contract"),
        ("Intern", "Intern"),
    ]
    employment_type = models.CharField(max_length=10, choices=EMPLOYMENT_TYPE_CHOICES)
    JOB_POSITION_CHOICES = [
        ("Manager", "Manager"),
        ("Developer", "Developer"),
        ("Designer", "Designer"),
        ("Analyst", "Analyst"),
        ("Tester", "Tester"),
        ("Project Manager", "Project Manager"),
        ("Software Engineer", "Software Engineer"),
        ("Data Scientist", "Data Scientist"),
        ("Data Analyst", "Data Analyst"),
        ("Quality Assurance Engineer", "Quality Assurance Engineer"),
        ("System Administrator", "System Administrator"),
        ("DevOps Engineer", "DevOps Engineer"),
        ("UI/UX Designer", "UI/UX Designer"),
        ("Product Manager", "Product Manager"),
        ("Sales Representative", "Sales Representative"),
        ("Marketing Specialist", "Marketing Specialist"),
        ("HR Manager", "HR Manager"),
        ("Customer Support Specialist", "Customer Support Specialist"),
        ("Technical Support Engineer", "Technical Support Engineer"),
        ("IT Support Specialist", "IT Support Specialist"),
        ("Content Writer", "Content Writer"),
        ("SEO Specialist", "SEO Specialist"),
        ("Finance Officer", "Finance Officer"),
        ("Accountant", "Accountant"),
        ("Operations Manager", "Operations Manager"),
        ("Business Analyst", "Business Analyst"),
        ("Network Engineer", "Network Engineer"),
        ("Cybersecurity Specialist", "Cybersecurity Specialist"),
        ("Machine Learning Engineer", "Machine Learning Engineer"),
        ("AI Researcher", "AI Researcher"),
        ("Database Administrator", "Database Administrator"),
    ]
    job_position = models.CharField(max_length=50, choices=JOB_POSITION_CHOICES)
    date_of_hire = models.DateField()
    date_of_termination = models.DateField(blank=True, null=True)
    DEPARTMENT_CHOICES = [
        ("Management", "Management"),
        ("Software Development", "Software Development"),
        ("Design", "Design"),
        ("Data Analysis", "Data Analysis"),
        ("Quality Assurance", "Quality Assurance"),
        ("Project Management", "Project Management"),
        ("Engineering", "Engineering"),
        ("Data Science", "Data Science"),
        ("Systems Administration", "Systems Administration"),
        ("DevOps", "DevOps"),
        ("Product Management", "Product Management"),
        ("Sales", "Sales"),
        ("Marketing", "Marketing"),
        ("Human Resources", "Human Resources"),
        ("Customer Support", "Customer Support"),
        ("Technical Support", "Technical Support"),
        ("IT Support", "IT Support"),
        ("Content Creation", "Content Creation"),
        ("SEO", "SEO"),
        ("Finance", "Finance"),
        ("Accounting", "Accounting"),
        ("Operations", "Operations"),
        ("Business Analysis", "Business Analysis"),
        ("Networking", "Networking"),
        ("Cybersecurity", "Cybersecurity"),
        ("Machine Learning", "Machine Learning"),
        ("Artificial Intelligence", "Artificial Intelligence"),
        ("Database Administration", "Database Administration"),
    ]
    department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES)

    # Salary Information
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    PAY_FREQUENCY_CHOICES = [
        ("Monthly", "Monthly"),
        ("Bi-Weekly", "Bi-Weekly"),
        ("Weekly", "Weekly"),
    ]
    pay_frequency = models.CharField(max_length=10, choices=PAY_FREQUENCY_CHOICES)
    bank_account_number = models.CharField(max_length=20)
    bank_name = models.CharField(max_length=100)
    bank_branch = models.CharField(max_length=100)

    # Emergency Contact Information
    emergency_contact_name = models.CharField(max_length=100)
    emergency_contact_relationship = models.CharField(max_length=50)
    emergency_contact_phone = models.CharField(
        max_length=10, validators=[validate_phone_number]
    )
    emergency_contact_address = models.TextField(blank=True, null=True)

    # Employment Status & History
    STATUS_CHOICES = [
        ("Active", "Active"),
        ("On Leave", "On Leave"),
        ("Terminated", "Terminated"),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    previous_positions = models.TextField(blank=True, null=True)

    # Additional Information
    profile_picture = models.ImageField(
        upload_to="profile_pictures/", blank=True, default="media/default.jpg"
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.employee_id:
            initials = f"{self.first_name[0]}{self.last_name[0]}".upper()
            random_digits = "".join(random.choices(string.digits, k=8))
            self.employee_id = f"{initials}{random_digits}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
