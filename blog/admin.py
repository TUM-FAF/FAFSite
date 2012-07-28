from django.contrib import admin 
from blog.models import Content

class ContentAdmin(admin.ModelAdmin):
	list_display = ('title', 'date')
	search_fields = ('title',)

admin.site.register(Content, ContentAdmin)
