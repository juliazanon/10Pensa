from django.urls import path
from django.conf.urls import url
from . import views



urlpatterns = [
    #perfil
    path('signup/', views.SignUpView.as_view(), name='signup'),
    #path('perfil_edit/', views.UserEditView.as_view(), name='perfil_edit'),
    path('perfil/', views.ProdutoListView.as_view(), name='perfil'),
    #produtos
    path('produto/novo/', views.ProdutoCreateView.as_view(), name='produto_new'),
    path('produto/<int:pk>/edit/', views.ProdutoUpdateView.as_view(), name='produto_edit'),
    path('produto/<int:pk>/delete/', views.ProdutoDeleteView.as_view(), name='produto_delete'),
    #receitas
    path('perfil/receitas/', views.ReceitaListView.as_view(), name='receitas'),
    path('perfil/receita/<int:pk>/', views.ReceitaDetailView.as_view(), name='receita_detail'),
    path('perfil/receitas/nova', views.ReceitaCreateView.as_view(), name='receita_new'),
    path('perfil/receita/<int:pk>/edit', views.ReceitaUpdateView.as_view(), name='receita_edit'),
    path('perfil/receita/<int:pk>/delete/', views.ReceitaDeleteView.as_view(), name='receita_delete'),
    #ingredientes
]