from django.urls import path

from . import views


urlpatterns = [
    path('', views.index),
    path('blog/', views.blog),
    path('blog/<post_id:int>', views.single_post),
    path('portfolio/', views.portfolio),
    path('portfolio/<project_id:int>', views.single_project),
    path('contacts/', views.contacts),
]
