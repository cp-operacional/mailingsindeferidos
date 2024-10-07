from django.contrib import admin
from django.urls import path, include
from indeferidos.views import IndeferidosListView, IndeferidosCountView
from address.views import FiltrarMunicipios, ListarUfs

urlpatterns = [
    path("admin/", admin.site.urls),
    path("indeferidos/", IndeferidosListView.as_view()),
    path("count/", IndeferidosCountView.as_view()),
    path('municipios/filtrar/', FiltrarMunicipios.as_view(), name='filtrar_municipios'),
    path('ufs/', ListarUfs.as_view(), name='listar_ufs'),
]
