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
    ('male','MALE'),
    ('female','FEMALE'),
)

class Classes(models.Model):
    name_of_class=models.CharField(max_length=100)
    monthly_fees=models.DecimalField(max_digits=10,decimal_places=2)
    subjects=models.CharField(max_length=50, choices=SUBJECT_CHOICES, default="")
    marks=models.CharField(max_length=100)
    total_students = models.CharField(max_length=50, default='')
    def __str__(self):
        return self.name_of_class


class Students(models.Model):
    name_of_student = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=20)
    adminssion_date = models.DateTimeField(auto_now_add=True)
    dob = models.DateField(max_length=8)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default="")
    address = models.CharField(max_length=300)
    father_name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=50)
    father_mobile_number = models.CharField(max_length=20)
