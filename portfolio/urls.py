from django.urls import path
from portfolio import views


urlpatterns = [
    path('', views.home, name='home'),
    path('projetos/', views.lista_projetos, name='projetos'),
    path('projetos/<str:id>/', views.detalhes_projeto, name='detalhes_projeto')
]
