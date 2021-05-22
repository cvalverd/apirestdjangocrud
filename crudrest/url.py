from django.urls import path
from .import views

urlpatterns = [
    path('', views.ProductosLista, name="productos"),
    path('detalle/<str:pk>', views.ProductosDetalle, name="detalle"),
    path('crear', views.ProductosCrear, name="crear"),
    path('actualizar/<str:pk>/', views.ProductosActualizar, name="actualizar"),
    path('eliminar/<str:pk>/', views.ProductosEliminar, name="eliminar"),
]
