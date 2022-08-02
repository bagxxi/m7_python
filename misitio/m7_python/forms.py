from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Comuna, Region, Inmuebles
from django.utils.translation import gettext_lazy as _


class UserForm(UserCreationForm):
    first_name = forms.CharField()
    first_name.label = 'Nombre'
    last_name = forms.CharField()
    last_name.label = 'Apellido'
    email = forms.EmailField()
    email.label = 'Correo Electrónico'

    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name','last_name', 'username', 'email', 'password1','password2' )
        labels = {'username': ('Nombre de usuario')}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'  # get or post
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-4 mb-0 mx-4'),
                Column('last_name', css_class='form-group col-md-4 mb-0 mx-4'),
                css_class='form-row'
            ),
            Row(
                Column('username', css_class='form-group col-md-4 mb-0 mx-4'),
                Column('email', css_class='form-group col-md-4 mb-0 mx-4'),
                css_class='form-row'
            ),
            Row(
                Column('password1', css_class='form-group col-md-4 mb-0 mx-4'),
                Column('password2', css_class='form-group col-md-4 mb-0 mx-4'),
                css_class='form-row'
            ),
            Submit('submit', 'Registrar usuario', css_class='form-group col-md-8 mb-0 mx-5 my-5')
        )



class TipoForm(forms.Form):
    tipos = ((1, 'Arrendatario'), (2, 'Arrendador'),)
    tipo = forms.ChoiceField(choices=tipos)
    rut = forms.CharField(label='rut', max_length=100)
    direccion = forms.CharField(label='direccion', max_length=100)
    telefono = forms.CharField(label='telefono', max_length=100)


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class InmuebleForm(forms.Form):
    tipos = ((1,"Casa"),(2,"Departamento"),(3,"Parcela"),(4,"Estacionamiento"),(5,"Otro"))
    id_tipo_inmueble = forms.ChoiceField(choices=tipos)
    comunas =  [(x.id,x.comuna)  for x in list(Comuna.objects.filter())]
    id_comuna = forms.ChoiceField(choices=comunas)
    regiones =  [(x.id,x.Region)  for x in list(Region.objects.filter())]
    id_region = forms.ChoiceField(choices=regiones)
    nombre_inmueble = forms.CharField(label='Nombre Inmueble', max_length=100)
    descripcion = forms.CharField(label='Descripcion del Inmueble', max_length=100)
    m2_construido = forms.CharField(label='M2 construidos', max_length=100)
    numero_banos = forms.CharField(label='Numero de Baños', max_length=100)
    numero_hab = forms.CharField(label='Numero de habitaciones', max_length=100)
    direccion = forms.CharField(label='Direccion', max_length=100)

class InmueblesUpdateForm(forms.ModelForm):
    class Meta:
        model=Inmuebles
        fields = ['nombre_inmueble', 'descripcion', 'm2_construido', 'numero_banos', 'numero_hab', 'direccion']

