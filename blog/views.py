from django.shortcuts import render
from blog.models import *
from shared import get_menu_items

menu_items = get_menu_items()


def achievements(request):
  global menu_items
  articles = Article.objects.filter(category='ACH').order_by('-date')
  return render(request, "timeline.html",
      {"activepage": "Achievements", "menu": menu_items, "articles": articles})


def activities(request):
  global menu_items
  articles = Article.objects.filter(category='ACT').order_by('-date')
  return render(request, "timeline.html",
      {"activepage": "Activities", "menu": menu_items, "articles": articles})


def blog(request):
  global menu_items
  articles = Article.objects.filter(category='BLOG').order_by('-date')
  return render(request, "timeline.html",
        {"activepage": "Activities", "menu": menu_items, "articles": articles})
