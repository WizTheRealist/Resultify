from django.contrib import admin
from .models import CustomUser, AdminHOD, Staffs, Faculty, Department, Courses, Students, Assessment

# Register the CustomUser model
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'user_type')
    list_filter = ('user_type',)
    search_fields = ('username', 'email')
    ordering = ('username',)

# Register the AdminHOD model
@admin.register(AdminHOD)
class AdminHODAdmin(admin.ModelAdmin):
    list_display = ('admin',)
    list_filter = ('created_at',)
    search_fields = ('admin__username', 'admin__email')
    ordering = ('created_at',)

# Register the Staffs model
@admin.register(Staffs)
class StaffsAdmin(admin.ModelAdmin):
    list_display = ('admin', 'address')
    list_filter = ('created_at',)
    search_fields = ('admin__username', 'admin__email')
    ordering = ('created_at',)

# Register the Faculty model
@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('faculty_name', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('faculty_name',)
    ordering = ('created_at',)

# Register the Department model
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_name', 'faculty_id')
    list_filter = ('faculty_id',)
    search_fields = ('department_name',)
    ordering = ('department_name',)

# Register the Courses model
@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'credit_unit', 'course_code')
    # list_filter = ('created_at')
    search_fields = ('course_name', 'course_code')
    ordering = ('course_name',)

# Register the Students model
@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'matric_number', 'course_id', 'session_start_year', 'session_end_year')
    list_filter = ('course_id', 'session_start_year', 'session_end_year')
    search_fields = ('first_name', 'last_name', 'matric_number')
    ordering = ('first_name',)

# Register the Assessment model
@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'mat_number', 'session', 'course_id', 'score', 'grade', 'created_at')
    search_fields = ['full_name', 'mat_number']
    list_filter = ['session', 'course_id']

