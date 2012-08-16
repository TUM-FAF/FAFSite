from django.contrib import admin 
from academics.models import User, UserMetaType, UserMeta, UserExtended, Empty
from django import forms

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

	def getAdditionalMeta(self):
		if self.userExtended != None:
			new_form = metaForm()
			new_form.setMeta(self.userExtended.getAttributes())
			# print self.userExtended.getAttributes()
			return new_form.as_p()

	'''
	UserMetaType.objects.all()				all meta types 
	self.userExtended.getAttributes()		user attributes (dict)

	TODO:
		use this function instead of getAdditionalMeta
		by doing this, getAdditionalMeta method and metaForm class
		try to use admin/includes/fieldset.html from change_form.html file
	'''
	def getAdditionalFieldsets(self):
		return None

class metaForm(forms.ModelForm):
	class Meta:
		model = Empty

	def __init__(self, *args, **kwargs):
		super(metaForm, self).__init__(*args, **kwargs)

	def setMeta(self, _meta):
		for meta in _meta:
			# import pdb
			# pdb.set_trace()
			meta_key = meta
			meta_value = _meta[meta]['value']
			meta_type = _meta[meta]['type']
			meta_data = _meta[meta]['data']

			if meta_type == 'number':
				form = forms.IntegerField()
			elif meta_type == 'string':
				form = forms.Textarea()
			# elif meta_type == 'choice':
			# 	form = forms.CharField(max_length=31, choices=meta_data)

			self.fields[meta_key] = form
			self.initial[meta_key] = meta_value
			self.changed_data.append(meta_key)
			self.base_fields[meta_key] = form
			self.declared_fields[meta_key] = form


class UserAdmin(admin.ModelAdmin):
	list_display = ('name', 'surname')
	search_fields = ('name', 'surname')
	form = UserAdminForm

	def save_model(self, request, obj, form, change):
		obj.save()	# User save
		# handling additional parameters
		# TODO: also check in here those attributes that allready do not exist for that
		#	user (meta data that is no longer needed for that user, will be deleted from
		#	template by JS and will be no longer in POST)
		userExtended = UserExtended(obj.id)
		for userMetaType in UserMetaType.objects.all():
			if userMetaType.key in request.POST:
				print request.POST[userMetaType.key]
				setattr(userExtended, userMetaType.key, request.POST[userMetaType.key])
				userExtended.save()

class UserMetaTypeAdmin(admin.ModelAdmin):
	list_display = ('key', 'type', 'multiple', 'data')
	search_fields = ('key', 'type')

class UserMetaAdmin(admin.ModelAdmin):
	list_display = ('user', 'meta', 'value')

admin.site.register(User, UserAdmin)
admin.site.register(UserMetaType, UserMetaTypeAdmin)
admin.site.register(UserMeta, UserMetaAdmin)