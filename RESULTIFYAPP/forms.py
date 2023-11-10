from django import forms
from django.contrib.auth.models import User

from RESULTIFYAPP.models import Courses, CustomUser
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser  # Your User model
        fields = ('username', 'email', 'password1', 'password2')

class DateInput(forms.DateInput):
    input_type = "date"

class AddStudentForm(forms.Form):
    email=forms.EmailField(label="Email",max_length=50,widget=forms.EmailInput(attrs={"class":"form-control"}))
    password=forms.CharField(label="Password",max_length=50,widget=forms.PasswordInput(attrs={"class":"form-control"}))
    first_name=forms.CharField(label="First Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name=forms.CharField(label="Last Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    matric_number = forms.CharField(label="Mat Number", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    username=forms.CharField(label="Username",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    address=forms.CharField(label="Address",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))

    def __init__(self, *args, **kwargs):
        super(AddStudentForm, self).__init__(*args, **kwargs)
        # courses = Courses.objects.all()
        # self.fields['course'].choices = [(course.id, course.course_name) for course in courses]

    # courses=Courses.objects.all()
    # course_list=[]
    # for course in courses:
    #    small_course=(course.id,course.course_name)
    #    course_list.append(small_course)

    gender_choice=(
        ("Male","Male"),
        ("Female","Female")
    )

#    course=forms.ChoiceField(label="Course",choices=course_list,widget=forms.Select(attrs={"class":"form-control"}))
    sex=forms.ChoiceField(label="Sex",choices=gender_choice,widget=forms.Select(attrs={"class":"form-control"}))
    session_start=forms.DateField(label="Session Start",widget=DateInput(attrs={"class":"form-control"}))
    session_end=forms.DateField(label="Session End",widget=DateInput(attrs={"class":"form-control"}))
    profile_pic=forms.FileField(label="Profile Pic",max_length=50,widget=forms.FileInput(attrs={"class":"form-control"}))

class EditStudentForm(forms.Form):
    email=forms.EmailField(label="Email",max_length=50,widget=forms.EmailInput(attrs={"class":"form-control"}))
    first_name=forms.CharField(label="First Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name=forms.CharField(label="Last Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    matric_number = forms.CharField(label="Mat Number", max_length=50,widget=forms.TextInput(attrs={"class": "form-control"}))
    username=forms.CharField(label="Username",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    address=forms.CharField(label="Address",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))

    def __init__(self, *args, **kwargs):
        super(EditStudentForm, self).__init__(*args, **kwargs)
        # courses = Courses.objects.all()
        # self.fields['course'].choices = [(course.id, course.course_name) for course in courses]
    courses=Courses.objects.all()
    course_list=[]
    for course in courses:
       small_course=(course.id,course.course_name)
       course_list.append(small_course)

    gender_choice=(
        ("Male","Male"),
        ("Female","Female")
    )

    course=forms.ChoiceField(label="Course",choices=course_list,widget=forms.Select(attrs={"class":"form-control"}))
    sex=forms.ChoiceField(label="Sex",choices=gender_choice,widget=forms.Select(attrs={"class":"form-control"}))
    session_start=forms.DateField(label="Session Start",widget=DateInput(attrs={"class":"form-control"}))
    session_end=forms.DateField(label="Session End",widget=DateInput(attrs={"class":"form-control"}))
    profile_pic=forms.FileField(label="Profile Pic",max_length=50,widget=forms.FileInput(attrs={"class":"form-control"}),required=False)

class FileUploadForm(forms.Form):
    file = forms.FileField()
