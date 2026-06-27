from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.views.generic import TemplateView, DetailView, ListView, View

from .models import Post, Category


# class HomeView(TemplateView):
#     template_name = "shop/home.html"

articles = [
    {"id": 1, "name": ""},
    {"id": 2, "name": "<h5>Article2</h5>"},
    {"id": 3, "name": "Article3"},
    {"id": 4, "name": "Article4"},
]


def home(request: HttpRequest):
    context = {
        "test_var": "hello world!",
        "articles": articles,
        "lst": ["apple", ]
    }


    return render(request, "shop/index.html", context)

def article_detail(request: HttpRequest, pk: int):
    article= next(x for x in articles if x["id"] == pk)
    return render(request, "article_detail.html", {"article": article})


def my_article_detail(request: HttpRequest):
    return HttpResponse(f"<b>Стаття ІНША</b>")

def year_archive(request: HttpRequest, year):
    return HttpResponse(f"<b>Рік: {year}</b>")


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse(f"<b>Стаття через ArticleView</b>")


class PostView(ListView):
    model = Post
    queryset = Post.objects.filter(is_published=True)
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["test_var"] = "secret"

        return context


    # pk_url_kwarg = 'article_pk' #Якщо параметр у URL має іншу назву,не 'pk'
