# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http  import HttpResponse
from appportfolio.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger	#paginacion

from django.contrib.auth import authenticate, get_user_model, login,logout  #todas son por defecto
from django.contrib.auth.decorators import login_required
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import redirect
from django.http import JsonResponse

################################################
# 1 - seguido
################################################
def seguido(request):
    lista_seguido = Seguido.objects.all()  # select * from Experiencias;
    page = request.GET.get('page')
    paginator = Paginator(lista_seguido, 3)  # 2 registros por página
    if page == None:
        print(" page recibe fuera de get o post NONE=" + str(page))
        page = paginator.num_pages
        request.session["pagina"] = page
    else:
        print(" page recibe esle del none de geo o post=" + str(page))
        request.session["pagina"] = page

    if request.method == 'GET':
        pagina = request.session["pagina"]
        print(" page recibe en GET=" + str(pagina))
    if request.method == 'POST':
        pagina = request.session["pagina"]
        print(" page recibe en POST=" + str(pagina))

    if "pagina" in request.session:
        page = request.session["pagina"]
        print(" page recibe de sesion=" + str(page))

    try:
        lista_seguido = paginator.get_page(page)
    except PageNotAnInteger:
        lista_seguido = paginator.page(1)
    except EmptyPage:
        lista_seguido = paginator.page(paginator.num_pages)

    context = {'lista_seguido': lista_seguido}
    return render(request, 'seguidos.html', context=context)

################################################
# 1 - seguidores
################################################

def seguidores(request):
    lista_seguidores = Seguidor.objects.all()  # select * from Experiencias;
    page = request.GET.get('page')
    paginator = Paginator(lista_seguidores, 2)  # 2 registros por página
    if page == None:
        print(" page recibe fuera de get o post NONE=" + str(page))
        page = paginator.num_pages
        request.session["pagina"] = page
    else:
        print(" page recibe esle del none de geo o post=" + str(page))
        request.session["pagina"] = page

    if request.method == 'GET':
        pagina = request.session["pagina"]
        print(" page recibe en GET=" + str(pagina))
    if request.method == 'POST':
        pagina = request.session["pagina"]
        print(" page recibe en POST=" + str(pagina))

    if "pagina" in request.session:
        page = request.session["pagina"]
        print(" page recibe de sesion=" + str(page))

    try:
        lista_seguidores = paginator.get_page(page)
    except PageNotAnInteger:
        lista_seguidores = paginator.page(1)
    except EmptyPage:
        lista_seguidores = paginator.page(paginator.num_pages)

    context = {'lista_seguidores': lista_seguidores}
    return render(request, 'seguidores.html', context=context)




################################################
# 1 - home
################################################

def home(request):
    '''
    habilidades = Habilidad.objects.all().order_by('id')
    formaciones = Formacion.objects.all().order_by('id')
    for r in habilidades:
        print(str(r.id) + " " + str(r.habilidad) + " " + str(r.nivel))
    for f in formaciones:
        print(str(f.id) + " " + str(f.estudio) + str(f.anyo))
    nombre="Bryan"
    context = {'habilidades': habilidades, 'formaciones':formaciones,'nombre':nombre}
    '''
    print("hola estoy en home") 
    nombre='Jonathan'
    edad=25
    telefono='674834567'
    context = {'nombre':nombre , 'edad':edad, 'telefono':telefono}
    return render(request, 'home.html', context=context)

################################################
# 2 - experiencias
################################################

def experiencias(request):
    lista_experiencias = Experiencia.objects.all()  # select * from Experiencias;
    page = request.GET.get('page')
    paginator = Paginator(lista_experiencias, 2)  # 2 registros por página
    if page == None:
        print(" page recibe fuera de get o post NONE=" + str(page))
        page = paginator.num_pages
        request.session["pagina"] = page
    else:
        print(" page recibe esle del none de geo o post=" + str(page))
        request.session["pagina"] = page

    if request.method == 'GET':
        pagina = request.session["pagina"]
        print(" page recibe en GET=" + str(pagina))
    if request.method == 'POST':
        pagina = request.session["pagina"]
        print(" page recibe en POST=" + str(pagina))

    if "pagina" in request.session:
        page = request.session["pagina"]
        print(" page recibe de sesion=" + str(page))

    try:
        lista_experiencias = paginator.get_page(page)
    except PageNotAnInteger:
        lista_experiencias = paginator.page(1)
    except EmptyPage:
        lista_experiencias = paginator.page(paginator.num_pages)

    context = {'lista_experiencias': lista_experiencias}
    return render(request, 'experiencias.html', context=context)

################################################
# 3 -  estudios
################################################

def estudios(request):
    estudios = Estudio.objects.all()
    return render(request, 'estudios.html', {'estudios': estudios})

################################################
# 4 -  habilidades
################################################

# def habilidades(request):
#     # Recuperar las habilidades desde la base de datos
#     habilidades = Habilidades.objects.all()

#     # Pasar las habilidades a la plantilla
#     return render(request, 'habilidades.html', {'habilidades': habilidades})




def habilidades(request):
    lista_habilidades = Habilidad.objects.all()  # select * from Experiencias;
    page = request.GET.get('page')
    paginator = Paginator(lista_habilidades, 2)  # 2 registros por página
    if page == None:
        print(" page recibe fuera de get o post NONE=" + str(page))
        page = paginator.num_pages
        request.session["pagina"] = page
    else:
        print(" page recibe esle del none de geo o post=" + str(page))
        request.session["pagina"] = page

    if request.method == 'GET':
        pagina = request.session["pagina"]
        print(" page recibe en GET=" + str(pagina))
    if request.method == 'POST':
        pagina = request.session["pagina"]
        print(" page recibe en POST=" + str(pagina))

    if "pagina" in request.session:
        page = request.session["pagina"]
        print(" page recibe de sesion=" + str(page))

    try:
        lista_habilidades = paginator.get_page(page)
    except PageNotAnInteger:
        lista_habilidades = paginator.page(1)
    except EmptyPage:
        lista_habilidades = paginator.page(paginator.num_pages)

    context = {'lista_habilidades': lista_habilidades}
    return render(request, 'habilidades.html', context=context)


################################################
# 5 -  sobremi
################################################

def sobremi(request):
    print("hola estoy en sobremi") 
    nombre='Jonathan'
    edad=25
    telefono='674834567'
    context = {'nombre':nombre, 'edad':edad, 'telefono':telefono}
    return render(request, 'sobremi.html', context=context)

################################################
# 6 -  diplomas
################################################

def diplomas(request):
    lista_diplomas = ''
    context = {'lista_diplomas': lista_diplomas}
    return render(request, 'diplomas.html', context=context)

################################################
# 7 -  certificados
################################################

def certificados(request):
    lista_certificados = ''
    context = {'lista_certificados': lista_certificados}
    return render(request, 'certificados.html', context=context)

################################################
# 8 -  enlaces
################################################

def enlaces(request):
    lista_urls = ''
    context = {'lista_urls': lista_urls}
    return render(request, 'enlaces.html', context=context)

'''
def formacion(request):
    formaciones = Formacion.objects.all().order_by('id')
    for f in formaciones:
        print(str(f.id) + " " + str(f.estudio) + str(f.anyo))
    context = {'formaciones': formaciones}
    return render(request, 'formacion.html', context=context)
'''

def ver_experiencia(request,id):
    expe_id=id
    experiencia = Experiencia.objects.get(id=expe_id)
    context = {'experiencia': experiencia}
    return render(request, 'ver_experiencia.html',context=context)

################################################
# Empresa
################################################

def empresa(request):
    # Obtener todas las empresas desde la base de datos
    empresas = Empresa.objects.all()

    # Pasar las empresas a la plantilla
    return render(request, 'empresa.html', {'empresas': empresas})

# ####################### NUEVAS ######################################################

#CERRAR LA SESION DEL USUARIO
def cerrar(request):
    username = request.user.username
    password = request.user.password
    idusuario = request.user.id
    print("logout.................. " + username + "clave=" + str(password) + "id=" + str(idusuario))
    user = authenticate(request, username=username, password=password)
    # desconectamos al usuario
    logout(request)
    return redirect('/')

def Login(request):
    nombre = 'John'  # Define the variable "nombre"
    clave = 'password'  # Define the variable "clave"
    request.user.username = nombre
    request.user.password = clave
    context = {'nombre': nombre, 'clave': clave}
    return render(request, 'home.html', context=context)


