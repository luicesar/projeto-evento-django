from django.urls import path
from agenda.views import index, exibir_evento

# URL da View: Agenda
urlpatterns = [
    path("", index),
    path("evento", exibir_evento)
]
