from django.shortcuts import render

from .models import Article

# Create your views here.


def index(request):
    latest_articles = Article.objects.all()
    return render(request, "news/article_list.html", {
        "page_title": "Latest Articles",
        "articles": latest_articles
    })


def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, "news/article_detail.html", {"article": article})
