from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('receitas.ursl')),
    path('admin/', admin.site.urls),
]
