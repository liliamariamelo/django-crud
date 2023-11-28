from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pessoa/', views.pessoa, name="pessoa"),
    path('pessoa/add', views.pessoa_add, name="pessoa_add"),
    path('pessoa/editar/<int:pessoa_pk>', views.pessoa_editar, name="pessoa_editar"),
    path('pessoa/excluir/<int:pessoa_pk>', views.pessoa_excluir, name="pessoa_excluir"),

]

