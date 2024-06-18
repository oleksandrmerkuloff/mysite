from django.urls import path

from . import views


urlpatterns = [
    path('', views.index),
    path('blog/', views.blog),
    path('portfolio/', views.portfolio),
    path('contacts/', views.contacts),
]
