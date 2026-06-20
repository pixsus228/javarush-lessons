from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
# from django.views.decorators.http import require_POST

# Create your views here.

def home(request: HttpRequest):
    # return render(request, "index.html", {
    #     "item_name": item.name # {{ item_name }} в html
    # })
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