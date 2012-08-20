from django.contrib import admin 
from academics.models import User, UserMetaType, UserMeta, UserExtended, Course
from django import forms
import json

def getMetaTypes():
	result = {}
	meta_types = UserMetaType.objects.all()
	for meta in meta_types:
		try:
			data = json.loads(meta.data)
		except:
			data = meta.data
		result[meta.key] = {'type': meta.type, 'data': data, 'value': ''}
	return result


class UserAdminForm(forms.ModelForm):
	userExtended = None
	class Meta:
		model = User

	def __init__(self, *args, **kwargs): # * - tuple, ** - dictionary
		super(UserAdminForm, self).__init__(*args, **kwargs)
		# Set the form fields based on the model object
		if kwargs.has_key('instance'):
			instance = kwargs['instance']	# User instance
			self.userExtended = UserExtended(kwargs['instance'].id)

	def getAdditionalFieldsets(self):
		if self.userExtended != None:
			meta_types = getMetaTypes()
			user_meta_types = self.userExtended.getAttributes()
			result = {}
			for key in meta_types:
				if key in user_meta_types:
					result[key] = user_meta_types[key]
				else:
					result[key] = meta_types[key]
			return result
		else:
			return getMetaTypes()


class UserAdmin(admin.ModelAdmin):
	list_display = ('name', 'surname')
	search_fields = ('name', 'surname')
	form = UserAdminForm

	def save_model(self, request, obj, form, change):
		obj.save()	# User save
		userExtended = UserExtended(obj.id)
		for userMetaType in UserMetaType.objects.all():
			if userMetaType.key in request.POST and request.POST[userMetaType.key] != '':
				if userMetaType.multiple:
					setattr(userExtended, userMetaType.key, request.POST.getlist(userMetaType.key))
				else:
					# print request.POST[userMetaType.key]
					setattr(userExtended, userMetaType.key, request.POST[userMetaType.key])					
				userExtended.save()
			else:
				userExtended.delMeta(userMetaType.key)

class UserMetaTypeAdmin(admin.ModelAdmin):
	list_display = ('key', 'type', 'multiple', 'data')
	search_fields = ('key', 'type')

	# save as a JSON object
	def save_model(self, request, obj, form, change):
		data = obj.data
		data = data.split(',')
		data = json.dumps(data)
		obj.data = data
		obj.save()


class UserMetaAdmin(admin.ModelAdmin):
	list_display = ('user', 'meta', 'value')

class CourseAdmin(admin.ModelAdmin):
	list_display = ('subject_en', 'subject_ro', 'semester')
	search_fields = ('subject',)

admin.site.register(User, UserAdmin)
admin.site.register(UserMetaType, UserMetaTypeAdmin)
admin.site.register(UserMeta, UserMetaAdmin)
admin.site.register(Course, CourseAdmin)