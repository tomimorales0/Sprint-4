import csv
import os

def validar_archivo():
    nombre_archivo = input("Ingrese nombre de cuenta: ")
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
        if not nombre_archivo.endswith('.csv'):
            print(f'Error:"{nombre_archivo}" No es un archivo CSV.')
            return
        if len(lineas) < 2: 
            print(f'Error:"{nombre_archivo}"No tiene datos.')
            return
        archivo.close() 
    return nombre_archivo 
    

def validar_dni():
    dni_cliente = input(str("Ingrese DNI:"))
    with open(cheques, "r", encoding="utf-8") as archivo_csv:
        categorias = csv.DictReader(archivo_csv)
        for rows in categorias:
            continue
        if rows["DNI"] != dni_cliente:
            print("Error: DNI No Registrado") 
            return 
    archivo_csv.close()      
    return dni_cliente

def validar_tipo_cheque():
    tipo_cheque = input("Ingrese tipo de cheque: ")
    return tipo_cheque

def validar_fechas():
    fecha_pago = input("Ingrese fecha de pago: ")
    return fecha_pago

def validar_salida():
    salida = input("Ingrese la salida: ")
    return salida

######################################
print("Bienvenido!\nPara acceder a sus cheques..")

cheques = validar_archivo()
print(f"Archivo: {cheques}")

dni = validar_dni()
print(f"DNI: {dni}") 

tipo_cheque = validar_tipo_cheque()
print(f"Tipo de Cheque: {tipo_cheque}") 

fechas = validar_fechas()
print(f"Fechas: {fechas}") 

salida = validar_salida()
print(f"Salida: {salida}") 
