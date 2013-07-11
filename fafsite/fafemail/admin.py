from django.contrib import admin
from fafemail.models import Email


class EmailAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'name', 'email')
    search_fields = ('name', 'email')

admin.site.register(Email, EmailAdmin)
