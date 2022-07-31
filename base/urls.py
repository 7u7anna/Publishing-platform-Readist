from django.urls import path
from . import views
from .views import ArticleView, ArticleReadView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

urlpatterns = [
    path('<int:pk>/delete-article/', ArticleDeleteView.as_view(), name='delete-article'),
    path('<int:pk>/update-article/', ArticleUpdateView.as_view(), name='update-article'),
    path('new-draft/', ArticleCreateView.as_view(), name='new-draft'),
    path('read/<int:pk>/', ArticleReadView.as_view(), name='read'),

    path('inspire/', views.inspire, name='inspire'),
    path('about/', views.about, name='about'),
    path('', ArticleView.as_view(), name='homepage'),
]