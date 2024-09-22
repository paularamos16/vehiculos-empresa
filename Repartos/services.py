from .models import *

def crear_vehiculo(patente, marca, modelo, year):
    vehiculo= Vehiculo.objects.create(patente=patente, marca=marca, modelo=modelo, year=year)
    if vehiculo:
        print (f"se ha creado create(rut=rut, nombre=nombre, apellido=apellido)")
    if chofer:
        print(f"se ha crado con exito el chofer {nombre} {apellido}")
    return chofer

def crear_registro_contable(fecha_compra, valor, vehiculo_id):
    habilitar_vehiculo(vehiculo_id)
    #Vehiculo.objects.filter(patente=vehiculo_id).update(activo=True)
    return RegistroContabilidad.objects.create(fecha_compra=fecha_compra, valor=valor, vehiculo_id=vehiculo_id)

def deshabilitar_chofer(rut):
    if isinstance(rut, Chofer):
        rut=rut.rut
    respuesta=Chofer.objects.filter(rut=rut).update(activo=False)
    if respuesta:
        print(f"se ha desabilitado con exito el chofer{rut}")
    return respuesta

def deshabilitar_vehiculo(patente):
    if isinstance(patente, Vehiculo):
        patente=patente.patente
    respuesta=Vehiculo.objects.filter(patente=patente).update(activo=False)
    if  respuesta:
        print(f"se ha deshabilitado con exito el vehiculo {patente}")
    return respuesta

def habilitar_chofer(rut):
    if isinstance(rut, Chofer):
        rut=rut.rut
    respuesta=Chofer.objects.filter(rut=rut).update(activo=True)
    if respuesta:
        print(f"se ha habilitado con exito el chofer{rut}")
    return respuesta

def habilitar_vehiculo(patente):
    if isinstance(patente, Vehiculo):
        patente=patente.patente
    respuesta=Vehiculo.objects.filter(patente=patente).update(activo=True)
    if respuesta:
        print(f"Se ha habilitado con exito el vehiculo {patente}")
    return respuesta

def obtener_vehiculo(patente):
    vehiculo = Vehiculo.objects.get(patente=patente)
    print(f"Patente:{vehiculo.patente} Marca: {vehiculo.marca} Modelo: {vehiculo.modelo} Año: {vehiculo.year}")
    return vehiculo

def obtener_chofer(rut):
    chofer = Chofer.objects.get(rut=rut)
    print(f"Rut:{chofer.rut} Nombre: {chofer.nombre} Apellido: {chofer.apellido} Activo: {chofer.activo}")
    return chofer

def asignar_chofer_a_vehiculo(chofer, vehiculo):
    if isinstance(chofer, Chofer):
        chofer= chofer.rut
    if isinstance(vehiculo, Vehiculo):
        vehiculo=vehiculo.patente    
    Chofer.objects.filter(rut=chofer).update(vehiculo_id=vehiculo)
    print(f"se ha asignado el chofer {chofer} al vehiculo {vehiculo}")

def imprimir_datos_vehiculos():
    vehiculos = Vehiculo.objects.all()
    for vehiculo in vehiculos:
        print(f"Patente:{vehiculo.patente} Marca: {vehiculo.marca} modelo: {vehiculo.modelo} Año: {vehiculo.year}")