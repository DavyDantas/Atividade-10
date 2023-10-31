from django.urls import path
from .views import *

urlpatterns = [
    path('', listarDiscos, name='listar_discos'),
    path('detalhes/<int:pk>', detalheDisco, name='detalhe_disco'),
    path('editar-disco/<int:pk>', edit_disco, name='edit_disco'),
    path('adicionar-disco', add_disco, name='add_disco'),
    path('deletar-disco/<int:pk>', delet_disco, name='delet_disco'),
]