from django.urls import path
from django.conf.urls import url
from . import views



urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('perfil_edit/', views.UserEditView.as_view(), name='perfil_edit'),
    path('perfil/', views.ProdutoListView.as_view(), name='perfil'),
    path('produto/novo/', views.ProdutoCreateView.as_view(), name='produto_new'),
    path('produto/<int:pk>/edit/', views.ProdutoUpdateView.as_view(), name='produto_edit'),
    path('produto/<int:pk>/delete/', views.ProdutoDeleteView.as_view(), name='produto_delete'),
    #url(r'^perfil/$', views.view_profile, name='view_profile'),
]