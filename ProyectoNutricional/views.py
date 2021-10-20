from django import forms
from django.shortcuts import redirect, render
from django.http import HttpRequest


from .forms import RecetaForm
from .models import Recetas

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
    """Renders the about page. cambiado para DB"""
    recetas= Recetas.objects.all()
    context={
        'recetas': recetas
    }
    assert isinstance(request, HttpRequest)
    
    return render(
        request,
        'recetas.html', 
        context    , 
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

def receta_form(request, id=0):
    if request.method == "GET":
        if id==0:  
            form = RecetaForm()
        else:    
            recetas = Recetas.objects.get(pk=id)
            form = RecetaForm(instance=recetas)
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'receta_form.html',{'form':form})
    else:
        if id==0:
            form = RecetaForm(request.POST)
        else:
            recetas = Recetas.objects.get(pk=id)
            form= RecetaForm(request.POST, instance=recetas)
        if form.is_valid():
            form.save()
        return redirect('recetas')


def receta_delete(request, id):
    recetas = Recetas.objects.get(pk=id)
    recetas.delete()
    return redirect('recetas')


        
        
    