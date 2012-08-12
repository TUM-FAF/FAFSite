from django.contrib import admin 
from academics.models import User, UserMetaType, UserMeta, UserExtended

class UserAdmin(admin.ModelAdmin):
	list_display = ('name', 'surname')
	search_fields = ('name', 'surname')

class UserMetaTypeAdmin(admin.ModelAdmin):
	list_display = ('key', 'type', 'multiple', 'data')
	search_fields = ('key', 'type')

class UserMetaAdmin(admin.ModelAdmin):
	list_display = ('user', 'meta', 'value')



admin.site.register(User, UserAdmin)
admin.site.register(UserMetaType, UserMetaTypeAdmin)
admin.site.register(UserMeta, UserMetaAdmin)
