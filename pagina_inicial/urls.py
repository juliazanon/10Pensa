from django.urls import path
from . import views
#from accounts import views as acc_views

urlpatterns = [
    path('', views.PaginaListView.as_view(), name='home'),
    path('produto/novo/', views.PaginaCreateView.as_view(), name='produto_new'),
    path('produto/<int:pk>/edit/', views.PaginaUpdateView.as_view(), name='produto_edit'),
    #path('perfil/', acc_views.perfil, name='perfil'),
]