from django.contrib import admin 
from academics.models import User, UserMetaKey, UserMeta

class UserAdmin(admin.ModelAdmin):
	list_display = ('name', 'surname')
	search_fields = ('name', 'surname')

class UserMetaKeyAdmin(admin.ModelAdmin):
	list_display = ('key', 'type', 'data')

class UserMetaAdmin(admin.ModelAdmin):
	list_display = ('user', 'meta', 'value')


admin.site.register(User, UserAdmin)
admin.site.register(UserMetaKey, UserMetaKeyAdmin)
admin.site.register(UserMeta, UserMetaAdmin)
