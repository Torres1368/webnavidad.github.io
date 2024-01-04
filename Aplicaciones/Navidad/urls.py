from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('vistaBelenes/', views.vistaBelenes, name='vistaBelenes'),
    path('vistaMusica/', views.vistaMusica, name='vistaMusica'),
    path('vistaCibeles/', views.vistaCibeles, name='vistaCibeles'),
    path('vistaDistritos/', views.vistaDistritos, name='vistaDistritos'),
    path('vistaJeronimos/', views.vistaJeronimos, name='vistaJeronimos'),
    path('vistaCabalgata/', views.vistaCabalgata, name='vistaCabalgata'),
    path('vistaIglesia/', views.vistaIglesia, name='vistaIglesia'),
    path('vistaMunicipales/', views.vistaMunicipales, name='vistaMunicipales'),
    path('vistaVilla/', views.vistaVilla, name='vistaVilla'),
    path('vistaJardines/', views.vistaJardines, name='vistaJardines'),
    path('vistaBalcones/', views.vistaBalcones, name='vistaBalcones'),
    path('vistaBalconesCasa/', views.vistaBalconesCasa, name='vistaBalconesCasa'),
    path('vistaMadridEstrella/', views.vistaMadridEstrella, name='vistaMadridEstrella'),
    path('vistaPistaHielo/', views.vistaPistaHielo, name='vistaPistaHielo'),
    path('vistaPlazaPaja/', views.vistaPlazaPaja, name='vistaPlazaPaja'),


]
