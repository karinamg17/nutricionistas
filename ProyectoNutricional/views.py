from os import kill
import re
from django.contrib.admin import options
import psycopg2

from django import forms
from django.contrib import auth
from django.shortcuts import redirect, render
from django.http import HttpRequest
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from operator import itemgetter

from .forms import AlimentoForm, RecetaForm
from .models import Recetas,Alimento,Usuarios
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
    cursor.execute("select u.nombre,u.primerapellido,u.segundoapellido,u.email,u.telefono,u.estado , c.f from (select idusuario , max(fechacita) as f from citas group by idusuario) c join usuarios u on u.idusuario=c.idusuario")
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

def crearusuario(request):
    """Renders the about page."""
    "usuarios= Usuarios.objects.all()"
    cursor = connection.cursor()
    cursor.execute("select usuarios.nombre,usuarios.primerapellido,usuarios.segundoapellido,usuarios.email,usuarios.telefono,usuarios.estado, citas.fechacita from usuarios join citas on usuarios.idusuario=citas.idusuario")
    results= cursor.fetchall()
    return render(request,'contactos.html', {'uniontablas': results})

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


"""
def paginicio(request):
    if request.method == "GET":
        return render(
                request,
                'pag-inicio.html',      
            )
    else:
        if request.method =='POST':
            email = request.POST.get('email')
            clave = request.POST.get('clave')

            try:
                user = Usuarios.empAuth_objects.get(email=email, clave=clave)
                if user is not None:
                    return render(
                request,
                'contactos.html',      
            )
                else:
                    print("Ingreso fallid")
                    return render(
                request,
                'crear-expediente.html',      
            )
            except Exception as identifier:
                return render(
                request,
                'recetas.html',      
            )
        else:
            return render(
                request,
                'alimentos.html',      
            )


"""
def paginicio(request):
    if request.method == "GET":
        return render(
                request,
                'pag-inicio.html',      
            )
    else:
        conn = psycopg2.connect(host="ec2-34-233-105-94.compute-1.amazonaws.com",
                                database="de6iseaflka80v",
                                user="lylnlnksouqxtc",
                                password="2c3fd1bac949f41306ba4d8857fdda5975091b8bbb4f95d2dfa7b0e8b37ddd41",
                                options="-c search_path=pln_schema")
        cursor = conn.cursor()
        conn2 = psycopg2.connect(host="ec2-34-233-105-94.compute-1.amazonaws.com",
                                database="de6iseaflka80v",
                                user="lylnlnksouqxtc",
                                password="2c3fd1bac949f41306ba4d8857fdda5975091b8bbb4f95d2dfa7b0e8b37ddd41",
                                options="-c search_path=pln_schema")
        cursor2 = conn2.cursor()
     
        cursor.execute("select usuario from usuarios;")
        cursor2.execute("select clave from usuarios;")
        e=[]
        p=[]
        for i in cursor:
            e.append(i)
        for j in cursor2:
            p.append(j)
       
        res = list(map(itemgetter(0),e))
        res2 = list(map(itemgetter(0),p))
        print (res)
        print(res2)
        if request.method =='POST':
            username = request.POST['username']
            password = request.POST['password']
            print('esto esta tomando el post' + username)
            print('esto esta tomando el post' + password)
            i=0
            k=len(res)
            while i<k:
                print ('esto esta tomando el while' + res[i])
                print ('esto esta tomando el while' +res2[i])
                if res[i] == username and res2[i]==password:
                    return render(request, 'index.html', {'username':username})
                    break
                i+=1
            else:
                return redirect('agendar')

            

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
        
    