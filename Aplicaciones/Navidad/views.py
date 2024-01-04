from django.shortcuts import render , redirect


# Create your views here.

def index(request):
    return render(request, 'index.html')

def vistaBelenes(request):
    return render (request, 'belenes.html')

def vistaMusica(request):
    return render (request, 'musica.html')

def vistaCibeles(request):
    return render (request, 'palacio_Cibeles.html')

def vistaDistritos(request):
    return render (request, 'distritos.html')

def vistaJeronimos(request):
    return render (request, 'jeronimos.html')

def vistaCabalgata(request):
    return render(request, 'cabalgata.html')

def vistaIglesia(request):
    return render(request, 'iglesia.html')

def vistaJardines(request):
    return render(request, 'jardines.html')

def vistaMunicipales(request):
    return render(request, 'municipales.html')

def vistaVilla(request):
    return render (request, 'villa.html')

def vistaBalcones(request):
    return render (request, 'balcones.html')

def vistaBalconesCasa(request):
    return render (request, 'balconesCasa.html')

def vistaMadridEstrella(request):
    return render (request, 'madridEstrella.html')

def vistaPistaHielo(request):
    return render (request, 'pistaHielo.html')

def vistaPlazaPaja(request):
    return render (request, 'plazaPaja.html')
