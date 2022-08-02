from django.shortcuts import render, redirect, resolve_url
from django.conf import settings
from m7_python.models import *
from m7_python.forms import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse,  HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from m7_python.forms import UserForm, TipoForm, UserUpdateForm, InmuebleForm, InmueblesUpdateForm


def indexView(request):
    Inm = Inmuebles.objects.all()
    return render(request, 'index.html', {'inmuebles':Inm})

def get_all_inmuebles():
    Inm = Inmuebles.objects.all()
    return Inm

def insertar_inmueble(data):
    id_user = data[0]
    id_tipo_inmueble = data[1]
    id_comuna = data[2]
    id_region = data[3]
    nombre_inmueble = data[4]
    descripcion = data[5]
    m2_construido = data[6]
    numero_banos = data[7]
    numero_hab = data[8]
    direccion = data[9]
    inm = Inmuebles(
        id_user = id_user,
        id_tipo_inmueble = id_tipo_inmueble,
        id_comuna = id_comuna,
        id_region = id_region,
        nombre_inmueble = nombre_inmueble,
        descripcion = descripcion,
        m2_construido = m2_construido,
        numero_banos = numero_banos,
        numero_hab = numero_hab,
        direccion = direccion)
    inm.save()

def actualizar_descrp_inmueble(id_inmueble,new_descrip):
    Inmuebles.objects.filter(pk=id_inmueble).update(descripcion=new_descrip)

def eliminar_inmueble(id_inmueble):
    Inmuebles.objects.get(id=id_inmueble).delete()

def registerView(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register_tipo?user='+str(form.cleaned_data['username']))
    else:
        form = UserForm()
    return render(request, 'registration/register.html', {'form': form})

def register_tipoView(request):
    username = request.GET['user']
    if request.method == 'POST':
        form = TipoForm(request.POST)
        if form.is_valid():
            form = TipoForm(request.POST)
            print(form)
            tipo = form.cleaned_data['tipo']
            rut = form.cleaned_data['rut']
            direccion = form.cleaned_data['direccion']
            telefono = form.cleaned_data['telefono']
            user = User.objects.filter(username=username)[0]
            tipo_user = Tipo_user.objects.filter(id=int(tipo))[0]
            datos = Profile(user=user, id_tipo_user=tipo_user, rut=rut, direccion=direccion, telefono=telefono)
            datos.save()
            return HttpResponseRedirect('/login/')
    else:
        form = TipoForm()
    return render(request, 'registration/register_tipo.html', {'form':form})

@login_required
def dashboardView(request):
    username = request.user
    current_user = request.user
    Inm = Inmuebles.objects.filter(id_user_id=current_user.id)
    return render(request, 'dashboard.html', {'inmuebles': Inm})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        if u_form.is_valid():
            u_form.save()
            return HttpResponseRedirect('/dashboard/')
    else:
        u_form = UserUpdateForm(instance=request.user.profile)
    context = {'u_form': u_form}
    return render(request, 'registration/update_profile.html', context)

@login_required
def new_inmuebleView(request):
    if request.method == 'POST':
        u_form = InmuebleForm(request.POST)
        if u_form.is_valid():
            u_form = InmuebleForm(request.POST)
            print(u_form)
            id_tipo_inmueble = u_form.cleaned_data['id_tipo_inmueble']
            id_comuna = u_form.cleaned_data['id_comuna']
            id_region = u_form.cleaned_data['id_region']
            nombre_inmueble = u_form.cleaned_data['nombre_inmueble']
            descripcion = u_form.cleaned_data['descripcion']
            m2_construido = u_form.cleaned_data['m2_construido']
            numero_banos = u_form.cleaned_data['numero_banos']
            numero_hab = u_form.cleaned_data['numero_hab']
            direccion = u_form.cleaned_data['direccion']
            print(u_form.cleaned_data)
            tipo_inmueble = Tipo_inmueble.objects.filter(id=int(id_tipo_inmueble))[0]
            comuna = Comuna.objects.filter(id=int(id_comuna))[0]
            reg = Region.objects.filter(id=int(id_region))[0]
            current_user = request.user
            user = User.objects.filter(id=current_user.id)
            inm = Inmuebles(id_tipo_inmueble=tipo_inmueble,
                            id_comuna=comuna,
                            id_region=reg,
                            nombre_inmueble=nombre_inmueble,
                            descripcion=descripcion,
                            m2_construido=m2_construido,
                            numero_banos=numero_banos,
                            numero_hab=numero_hab,
                            direccion=direccion)
            print(user)
            inm.id_user_id = current_user.id
            inm.save()
            return HttpResponseRedirect('/dashboard/')
    else:
        u_form = InmuebleForm()
    context = {'u_form': u_form}
    return render(request, 'new_inmueble.html', context)

@login_required
def inmuebles_update(request):
    inmueble_id = request.GET['id_inmueble']
    if request.method == 'POST':
        inmueble_id = request.GET['id_inmueble']
        inmueble = Inmuebles.objects.filter(id=inmueble_id).first()
        u_form = InmueblesUpdateForm(request.POST,instance=inmueble)
        if u_form.is_valid():
            u_form.save()
            return HttpResponseRedirect('/dashboard/')
        else:
            u_form = InmueblesUpdateForm(instance=request.user.profile)
        context={'u_form': u_form}
        return render(request, 'registration/update_profile.html', context)