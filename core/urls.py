from django.contrib import admin
from django.urls import path, include
from indeferidos.views import IndeferidosListView
urlpatterns = [
    path("admin/", admin.site.urls),
    path("indeferidos/", IndeferidosListView.as_view()),
]
