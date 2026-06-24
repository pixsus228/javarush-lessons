from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.views.generic import TemplateView, DetailView, ListView, View

from .models import Post, Category


class HomeView(TemplateView):
    template_name = "shop/home.html"


def home(request: HttpRequest):
    return render(request, "index.html", context={
        "item_name": item.name # {{ item_name }} в html
    })
    print(request.GET)

    return HttpResponse(f"<b>Home</b>")

    if "success":
        redirect("shop:home")

def article_detail(request: HttpRequest, pk: int):
    return HttpResponse(f"<b>Стаття: {pk}</b>")


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