from django.urls import path
from .views import NewsListView, NewsDetailView, NewCreateView, NewEditView

urlpatterns = [
    path(
        'news',
        NewsListView.as_view(),
        name='news_list',
    ),
    path(
        'news/<int:pk>',
        NewsDetailView.as_view(),
        name='news_detail',
    ),
    path(
        'news/creating',
        NewCreateView.as_view(),
        name='create_new',
    ),
    path(
        'news/<int:new_id>/editing',
        NewEditView.as_view(),
        name='edit_new',
    ),
]
