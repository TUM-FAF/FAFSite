from django.contrib import admin 
from academics.models import User, UserMetaKey, UserMeta

class UserAdmin(admin.ModelAdmin):
	list_display = ('name', 'surname')
	search_fields = ('name', 'surname')

class UserMetaKeyAdmin(admin.ModelAdmin):
	list_display = ('meta_key', 'meta_type', 'meta_data')

class UserMetaAdmin(admin.ModelAdmin):
	list_display = ('key', 'value')


# class ProfessorAdmin(admin.ModelAdmin):
# 	list_display = ('name', 'surname', 'rank')
# 	search_fields = ('name', 'surname',)

# class StudentAdmin(admin.ModelAdmin):
# 	list_display = ('name', 'surname', 'group')
# 	search_fields = ('name', 'surname',)

# class AlumniAdmin(admin.ModelAdmin):
# 	list_display = ('name', 'surname', 'group')
# 	search_fields = ('name', 'surname',)

# class CourseAdmin(admin.ModelAdmin):
# 	list_display = ('subject_en', 'subject_ro', 'semester')
# 	search_fields = ('semester',)

admin.site.register(User, UserAdmin)
admin.site.register(UserMetaKey, UserMetaKeyAdmin)
admin.site.register(UserMeta, UserMetaAdmin)

# admin.site.register(Professor, ProfessorAdmin)
# admin.site.register(Student, StudentAdmin)
# admin.site.register(Alumni, AlumniAdmin)
# admin.site.register(Course, CourseAdmin)
