from django.urls import path
from .views import PageListView, PageDetailView

urlpatterns = [
    path('pages/', PageListView.as_view(), name='page-list'),
    path('page/<slug>/', PageDetailView.as_view(), name='page-detail'),
]
