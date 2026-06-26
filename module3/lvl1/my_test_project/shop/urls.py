from django.urls import path, re_path

from .views import (
    home,
    ArticleView,
    PostView,

    year_archive,
    article_detail
)

app_name = "shop"

urlpatterns = [
    # path('', HomeView.as_view(), name='home'),
    path('', home, name='home'),

    # ПОРЯДОК ВАЖЛИВИЙ
    path('articles/', ArticleView.as_view(), name='articles'),
    path('articles/<int:pk>', article_detail, name='articles_detail'),

    # posts
    path('posts/', PostView.as_view(), name="posts"),

    re_path(r'^articles/(?P<year>[0-9]{4})/$', year_archive),
    # re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive)
]