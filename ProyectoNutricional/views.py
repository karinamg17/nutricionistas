from django import forms
from django.shortcuts import redirect, render
from django.http import HttpRequest


from .forms import AlimentoForm, RecetaForm
from .models import Recetas,Alimento
from django.db import connection

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


def buscar(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'buscar.html',
        
    )


def contactos(request):
    """Renders the about page."""
    "usuarios= Usuarios.objects.all()"
    cursor = connection.cursor()
    cursor.execute("select usuarios.nombre,usuarios.primerapellido,usuarios.segundoapellido,usuarios.email,usuarios.telefono,usuarios.fecha_creacion,usuarios.estado , citas.fechacita from usuarios join citas on usuarios.idusuario=citas.idusuario")
    results= cursor.fetchall()
    return render(request,'contactos.html', {'uniontablas': results})
    """context={
        'usuarios': usuarios,
    }
    assert isinstance(request, HttpRequest)
   
    return render(
        request,
        'contactos.html',
        context    ,
    ) """


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

def alimentos(request):
    """Renders the about page."""
    alimento= Alimento.objects.all()
    context={
        'alimento': alimento
    }

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'alimentos.html',
        context,
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



def alimentos_form(request, id=0):
    if request.method == "GET":
        if id==0:  
            form = AlimentoForm()
        else:    
            alimento = Alimento.objects.get(pk=id)
            form = AlimentoForm(instance=alimento)
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'alimentos_form.html',{'form':form})
    else:
        if id==0:
            form = AlimentoForm(request.POST)
        else:
            alimento = Alimento.objects.get(pk=id)
            form= AlimentoForm(request.POST, instance=alimento)
        if form.is_valid():
            form.save()
        return redirect('alimentos')


def alimento_delete(request, id):
    alimento = Alimento.objects.get(pk=id)
    alimento.delete()
    return redirect('alimentos')        
        
    