from django.urls import path
from . import views

urlpatterns = [
    path('', views.PaginaListView.as_view(), name='home'),
    path('produto/new/', views.PaginaCreateView.as_view(), name='produto_new'),
    path('produto/<int:pk>/edit/', views.PaginaUpdateView.as_view(), name='produto_edit'),
]