from django.urls import path
from .views import home_view,article_view,articles_view

urlpatterns = [
    path("",home_view,name="home"),
    path("article/<int:pk>/",article_view,name="article"),
    path("articles/",articles_view,name="articles"),

]
