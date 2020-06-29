from django.db import models

# Create your models here.

SUBJECT_CHOICES = (
    ('python','PYTHON'),
    ('django', 'DJANGO'),
    ('java','JAVA'),
    ('dotnet','DOTNET'),
    ('node.js','NODE.JS'),
)

GENDER_CHOICES =(
    ('Male','MALE'),
    ('Female','FEMALE'),
)

EMPLOYEE_TYPE = (
    ('Teaching Staff','TEACHING STAFF'),
    ('Non-Teaching','NON-TEACHING'),
)

class Info(models.Model):
    institute_name = models.CharField(max_length=100)
    target_line = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    website_name = models.CharField(max_length=100)
    address = models.CharField(max_length=300)


class Students(models.Model):
    name_of_student = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=20)
    adminssion_date = models.DateTimeField(auto_now_add=True)
    dob = models.DateField(max_length=8)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default="")
    address = models.CharField(max_length=300)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100, default="")
    father_occupation = models.CharField(max_length=50)
    mother_occupation = models.CharField(max_length=50, default="")
    father_mobile_number = models.CharField(max_length=20)
    username = models.CharField(max_length=50, default="")
    password = models.CharField(max_length=50, default="")
    def __str__(self):
        return self.name_of_student


class Classes(models.Model):
    name_of_class=models.CharField(max_length=100)
    monthly_fees=models.DecimalField(max_digits=10,decimal_places=2)
    subjects=models.CharField(max_length=50, choices=SUBJECT_CHOICES)
    marks=models.CharField(max_length=100)
    total_students = models.CharField(max_length=50, default='')
    reg_no = models.ForeignKey(Students, on_delete=models.CASCADE, null=True, default="")
    def __str__(self):
        return self.name_of_class


class Employee(models.Model):
    name_of_employee = models.CharField(max_length=100)
    joining_date = models.DateField(max_length=10)
    dob = models.DateField(max_length=10)
    Employee_type = models.CharField(max_length=30, choices=EMPLOYEE_TYPE)
    monthly_salary = models.IntegerField()
    mobile_number = models.CharField(max_length=20)
    father_name = models.CharField(max_length=100)
    experience = models.CharField(max_length=50)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    email = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    def __str__(self):
        return self.name_of_employee
