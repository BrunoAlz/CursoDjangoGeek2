from django.urls import path

# Fazemos o import da CBV criado la em *core - views.py*
from .views import ErrorView, IndexView

urlpatterns = [
    #Caminho '' = RAIZ, IndexView é a Classe, e o nome 
    path('', IndexView.as_view(), name='index'),
    path('error/', ErrorView.as_view(), name='error'),
]
