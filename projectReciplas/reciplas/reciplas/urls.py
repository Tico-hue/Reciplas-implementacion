"""reciplas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from . import views
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Login',views.mostrarLogin, name = 'login'),
    path('',views.mostrarInicio, name = 'inicio'),
   
    
    # path('Crear/', views.Crear.as_view(), name="crear"),
	# path('Modificar/<str:pk>', views.Modificar.as_view(), name="modificar"),
	# path('Eliminar/<str:pk>', views.Eliminar.as_view(), name="eliminar"),
    path('proveedores',views.CtrlEditarProveedor.mostrarProveedores, name = 'proveedores'),
    # path('crear_prov/',views.crearProveedor, name = 'crearProveedor'),
    path('guardar/<str:id>',views.CtrlEditarProveedor.guardarForm, name = 'guardar'),
    path('proveedores/editar_prov/<str:id>',views.CtrlEditarProveedor.mostrarForm, name = 'editarProveedor'),

]
