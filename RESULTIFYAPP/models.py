from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.
class CustomUser (AbstractUser):    # Define a custom user model class named CustomUser, inheriting from AbstractUser
    user_type_data = ((1,"HOD"),(2,"Staff"),(3,"Student"))      # Define user_type_data as a tuple of choices for the 'user_type' field
    user_type = models.CharField(default=1,choices=user_type_data,max_length=10)        # Define a CharField 'user_type' with default value 1 and choices restricted to user_type_data
    groups = models.ManyToManyField('auth.Group', related_name='customuser_set')        # Define a ManyToManyField 'groups' to associate the user with groups
    user_permissions = models.ManyToManyField('auth.Permission', related_name='customuser_set')         # Define a ManyToManyField 'user_permissions' to associate the user with permissions


class AdminHOD (models.Model):  # Define the 'AdminHOD' model class
    id = models.AutoField(primary_key=True) # Define a primary key field 'id' with auto-incrementing behavior
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)    # Define a one-to-one relationship with the 'CustomUser' model, indicating that each AdminHOD is associated with one CustomUser
    created_at = models.DateTimeField(auto_now_add=True)    # Define a 'created_at' field to store the creation date and time with auto_now_add=True
    updated_at = models.DateTimeField(auto_now=True)    # Define an 'updated_at' field to store the last update date and time with auto_now=True
    objects = models.Manager()  # Define the 'objects' attribute with the default manager

class Staffs (models.Model):    # Define the 'Staffs' model class
    id = models.AutoField(primary_key=True) # Define a primary key field 'id' with auto-incrementing behavior
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)   # Define a one-to-one relationship with the 'CustomUser' model, indicating that each staff member is associated with one CustomUser
    address = models.TextField()    # Define an 'address' field to store the address of the staff member as text
    created_at = models.DateTimeField(auto_now_add=True)    # Define a 'created_at' field to store the creation date and time with auto_now_add=True
    updated_at = models.DateTimeField(auto_now=True)    # Define an 'updated_at' field to store the last update date and time with auto_now=True
    objects = models.Manager()  # Define the 'objects' attribute with the default manager

class Faculty(models.Model):
    id = models.AutoField(primary_key=True)  # Define a primary key field 'id' with auto-incrementing behavior
    faculty_name = models.CharField(max_length=255)  # Define a 'faculty_name' field to store the name of the faculty with a maximum length of 255 characters
    created_at = models.DateTimeField(auto_now_add=True)  # Define a 'created_at' field to store the creation date and time with auto_now_add=True
    updated_at = models.DateTimeField(auto_now=True)  # Define an 'updated_at' field to store the last update date and time with auto_now=True
    objects = models.Manager()  # Define the 'objects' attribute with the default manager

class Department(models.Model):
    id = models.AutoField(primary_key=True)  # Define a primary key field 'id' with auto-incrementing behavior
    department_name = models.CharField(max_length=255)  # Define a 'department_name' field to store the name of the department with a maximum length of 255 characters
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)  # Define a foreign key field 'faculty_id' to associate the department with a Faculty, using CASCADE for automatic deletion if the related Faculty is deleted
    objects = models.Manager()  # Define the 'objects' attribute with the default manager

class Courses(models.Model):
    id = models.AutoField(primary_key=True)  # Define a primary key field 'id' with auto-incrementing behavior
    course_name = models.CharField(max_length=255)  # Define a 'course_name' field to store the name of the course with a maximum length of 255 characters
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    credit_unit = models.CharField(max_length=1)  # Define an 'credit_unit' field to store the credit units of the course
    course_code = models.CharField(max_length=10, unique=True)  # Define a 'course_code' field to store the code of the course with a maximum length of 10 characters
    # staff_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Define a foreign key field 'staff_id' to associate the course with a CustomUser, using CASCADE for automatic deletion if the related CustomUser is deleted
    created_at = models.DateTimeField(auto_now_add=True)  # Define a 'created_at' field to store the creation date and time with auto_now_add=True
    updated_at = models.DateTimeField(auto_now=True)  # Define an 'updated_at' field to store the last update date and time with auto_now=True
    objects = models.Manager()  # Define the 'objects' attribute with the default manager

class Students(models.Model):
    id = models.AutoField(primary_key=True)  # Define a primary key field 'id' with auto-incrementing behavior
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)  # Define a one-to-one relationship with the 'CustomUser' model, indicating that each student is associated with one CustomUser and using CASCADE for automatic deletion if the related CustomUser is deleted
    first_name = models.CharField(max_length=30)  # Define a 'first_name' field to store the first name of the student with a maximum length of 30 characters
    last_name = models.CharField(max_length=30)  # Define a 'last_name' field to store the last name of the student with a maximum length of 30 characters
    matric_number = models.CharField(max_length=30)  # Define a 'matric_number' field to store the matriculation number of the student with a maximum length of 30 characters
    gender = models.CharField(max_length=255)  # Define a 'gender' field to store the gender of the student with a maximum length of 255 characters
    profile_pic = models.FileField()  # Define a 'profile_pic' field to store the profile picture of the student
    address = models.TextField()  # Define an 'address' field to store the address of the student as text
    course_id = models.ForeignKey(Courses, on_delete=models.DO_NOTHING)  # Define a foreign key field 'course_id' to associate the student with a course (Courses model) without any automatic deletion action (DO_NOTHING)
    session_start_year = models.DateField()  # Define a 'session_start_year' field to store the start year of the student's session
    session_end_year = models.DateField()  # Define a 'session_end_year' field to store the end year of the student's session
    created_at = models.DateTimeField(auto_now_add=True)  # Define a 'created_at' field to store the creation date and time with auto_now_add=True
    updated_at = models.DateTimeField(auto_now=True)  # Define an 'updated_at' field to store the last update date and time with auto_now=True
    objects = models.Manager()  # Define the 'objects' attribute with the default manager

SESSION_CHOICES = (
    ('2001/2002', '2001/2002'), ('2003/2004', '2003/2004'), ('2005/2006', '2005/2006'), ('2007/2008', '2007/2008'),
    ('2009/2010', '2009/2010'), ('2011/2012', '2011/2012'), ('2013/2014', '2013/2014'), ('2015/2016', '2015/2016'),
    ('2017/2018', '2017/2018'), ('2019/2020', '2019/2020'), ('2021/2022', '2021/2022'), ('2023/2024', '2023/2024'),
)
class Assessment(models.Model):
    id = models.AutoField(primary_key=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="student")
    session = models.CharField(_('session'), choices=SESSION_CHOICES,
                               max_length=10, default='2012/2014')
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
    # uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="uploaded_by")
    created_at = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=30)
    mat_number = models.CharField(max_length=20)
    score = models.IntegerField(_('score'))
    grade = models.CharField(max_length=2)


# Define a signal handler to create user profiles after a CustomUser instance is created
@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:  # Check if a new instance of CustomUser has been created
        if instance.user_type == 1:
            # If the user type is 1 (HOD), create an AdminHOD instance associated with the user
            AdminHOD.objects.create(admin=instance)
        elif instance.user_type == 2:
            # If the user type is 2 (Staff), create a Staffs instance associated with the user, with an empty address
            Staffs.objects.create(admin=instance, address="")
        elif instance.user_type == 3:
            # If the user type is 3 (Student), create a Students instance associated with the user, with default values
            Students.objects.create(admin=instance, first_name="", last_name="", mat_number="", course_id=Courses.objects.get(id=1), session_start_year="", session_end_year="", address="", profile_pic="", gender="")

# Define a signal handler to save user profiles after a CustomUser instance is saved
@receiver(post_save,sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.adminhod.save()  # Save the associated AdminHOD instance
    elif instance.user_type == 2:
        instance.staffs.save()  # Save the associated Staffs instance
    elif instance.user_type == 3:
        instance.students.save()  # Save t