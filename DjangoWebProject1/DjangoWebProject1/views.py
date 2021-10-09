from django.shortcuts import render
from django.http import HttpRequest

def index(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'index.html', 
    )

def agendar(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'agendar.html',
    )


def alimentos(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'alimentos.html',
    )


def buscar(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'buscar.html',
        
    )


def contactos(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'contactos.html',
        
    )


def crearexpediente(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'crear-expediente.html',
        
    )



def verexpediente(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'ver-expediente.html',
        
    )

def recetas(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'recetas.html',      
    )



def pagbloqueada(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'pag-bloqueada.html',      
    )

def paginicio(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'pag-inicio.html',      
    )

def pagolvido(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'pag-olvido.html',      
    )

def pagregistro(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'pag-registro.html',      
    )