from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'date')
    search_fields = ('category', 'title',)


admin.site.register(Article, ArticleAdmin)
