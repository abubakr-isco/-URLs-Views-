from django.urls import path
from . import views

urlpatterns = [
    path("articles/", views.ArticleListView.as_view(), name="article_list"),
    path("articles/<int:pk>/", views.ArticleDetailView.as_view(), name="article_detail"),
    path("category/<str:slug>/", views.CategoryDetailView.as_view(), name="category_detail"),
]
