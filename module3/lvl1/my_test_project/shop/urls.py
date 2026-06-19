from django.urls import path, re_path

from . import views

app_name = "shop"

urlpatterns = [
    path('', views.home, name='home'),

    # ПОРЯДОК ВАЖЛИВИЙ
    path('articles/500', views.my_article_detail, name='about'),
    path('articles/<int:pk>', views.article_detail, name='about'),

    re_path(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),
    # re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive)
]