from django.contrib import admin 
from academics.models import Professor, Student, Alumni, Course

class ProfessorAdmin(admin.ModelAdmin):
	list_display = ('name', 'surname', 'rank')
	search_fields = ('name', 'surname',)

class StudentAdmin(admin.ModelAdmin):
	list_display = ('name', 'surname', 'group')
	search_fields = ('name', 'surname',)

class AlumniAdmin(admin.ModelAdmin):
	list_display = ('name', 'surname')
	search_fields = ('name',)

class CourseAdmin(admin.ModelAdmin):
	list_display = ('subject_en', 'subject_ro', 'semester')
	search_fields = ('semester',)

admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Alumni, AlumniAdmin)
admin.site.register(Course, CourseAdmin)
