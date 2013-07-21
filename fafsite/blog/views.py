from django.shortcuts import render

from .models import Article


def achievements(request):
    global menu_items
    articles = Article.objects.filter(category='ACH').order_by('-date')
    return render(request, "timeline.html",
                  {"activepage": "Achievements",
                   "articles": articles})


def activities(request):
    global menu_items
    articles = Article.objects.filter(category='ACT').order_by('-date')
    return render(request, "timeline.html",
                  {"activepage": "Activities",
                   "articles": articles})
