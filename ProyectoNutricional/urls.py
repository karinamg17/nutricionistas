"""
DjangoWebProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Uncomment next two lines to enable admin:
from django.contrib import admin
from django.urls import path

from ProyectoNutricional import views


urlpatterns = [
    path('', views.index, name='index'),
    path('agendar/',views.agendar,name='agendar'),
    path('alimentos/',views.alimentos,name='alimentos'),
    path('buscar/',views.buscar,name='buscar'),
    path('contactos/',views.contactos,name='contactos'),
    path('crear-expediente/',views.crearexpediente,name='crear-expediente'),
    path('ver-expediente/',views.verexpediente,name='ver-expediente'),
    path('recetas/',views.recetas,name='recetas'), #ver recetas
    path('pag-bloqueada/',views.pagbloqueada,name='pag-bloqueada'),
    path('pag-olvido/',views.pagolvido,name='pag-olvido'),
    path('pag-inicio/',views.paginicio,name='pag-inicio'),
    path('pag-registro/',views.pagregistro,name='pag-registro'),
    path('receta_form',views.receta_form,name='receta_form'), #agregar recetas
    path('<int:id>/',views.receta_form,name='receta_update'), #actualizar recetas
    path('delete/<int:id>/',views.receta_delete,name='receta_delete'), #actualizar recetas
    path('admin/', admin.site.urls),
]
