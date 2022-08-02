import os
import time
import django

from m7_python.models import Inmuebles, Region

os.environ.setdefault("DJANGO_SETTINGS_MODULE","misitio.settings")
django.setup()

def get_list_inmuebles(name, descr):
    lista_inmuebles = Inmuebles.objects.filter(nombre__contains=name).filter(descripcion__contains=descr)
    archi1 = open("datos.txt", "w")
    for l in lista_inmuebles:
            archi1.write(str(l))
            archi1.write("\n")
    archi1.close()

def get_list_inmuebles(comuna):
    select = """
        select      A.id,
                    A.nombre_inmueble,
                    A.descripcion
        from        public.m7_python_inmuebles  A
        inner join  public.m7_python_region     B
        on          A.id_region_id = B.id
        inner join  public.m7_python_comuna     C
        on          A.id_comuna_id = C.id
        where       C.comuna like '%"""+str(comuna)+"""%'
        """
    query = Inmuebles.objects.raw(select)
    archi1=open("datos.txt", "w")
    for p in query:
        archi1.write(p.nombre_inmueble+','+p.descripcion)
        archi1.write("\n")
    archi1.close()

def get_list_inmuebles_region(id):
    for i in range(1, 15):
        region = str(Region.objects.filter(id=i).get())
        lista_inmuebles = Inmuebles.objects.filter(id=i)
        archi1 = open("datos.txt", "a")
        for l in lista_inmuebles:
            archi1.write(str(l))
            archi1.write(',')
            archi1.write(region)
            archi1.write("\n")
        archi1.close()

