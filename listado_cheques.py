import csv
import argparse
import os
from datetime import datetime

# Timestamp a fecha legible
def timestamp_to_date(timestamp):
    return datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d')

# Filtrar
def filtrar_cheques(data, dni, tipo_cheque, estado=None, fecha_inicio=None, fecha_fin=None):
    cheques_filtrados = []
    
    for cheque in data:
        if cheque['DNI'] != dni:
            continue
        if cheque['TipoCheque'].upper() != tipo_cheque.upper():
            continue
        if estado and cheque['Estado'].upper() != estado.upper():
            continue
        if fecha_inicio and int(cheque['FechaOrigen']) < fecha_inicio:
            continue
        if fecha_fin and int(cheque['FechaOrigen']) > fecha_fin:
            continue
        
        cheques_filtrados.append(cheque)
    
    return cheques_filtrados

# //export to csv
def exportar_a_csv(data, dni):
    timestamp_actual = int(datetime.now().timestamp())
    nombre_archivo = f"{dni}_{timestamp_actual}.csv"
    with open(nombre_archivo, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    print(f"Datos exportados a {nombre_archivo}")

# Lectura y procesamiento del archivo CSVd
def procesar_cheques(archivo_csv, dni, salida, tipo_cheque, estado=None, fecha_inicio=None, fecha_fin=None):
    try:
        with open(archivo_csv, mode='r') as file:
            reader = csv.DictReader(file)
            data = list(reader)  # Leer todo el archivo como una lista de diccionarios
        
        # Filtrar cheques:
        cheques_filtrados = filtrar_cheques(data, dni, tipo_cheque, estado, fecha_inicio, fecha_fin)
        
        if not cheques_filtrados:
            print("No se encontraron cheques que coincidan con los criterios de búsqueda.")
            return
        
        if salida == 'PANTALLA':
            for cheque in cheques_filtrados:
                cheque['FechaOrigen'] = timestamp_to_date(cheque['FechaOrigen'])
                cheque['FechaPago'] = timestamp_to_date(cheque['FechaPago'])
                print(cheque)
        elif salida == 'CSV':
            exportar_a_csv(cheques_filtrados, dni)
        else:
            print("El parámetro de salida debe ser 'PANTALLA' o 'CSV'.")
    
    except FileNotFoundError:
        print(f"El archivo {archivo_csv} no existe.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Configuración de los argumentos de l.comandos
def main():
    parser = argparse.ArgumentParser(description='Procesar cheques bancarios.')
    parser.add_argument('archivo_csv', type=str, help='Nombre del archivo CSV a procesar.')
    parser.add_argument('dni', type=str, help='DNI del cliente.')
    parser.add_argument('salida', choices=['PANTALLA', 'CSV'], help='Dónde mostrar la salida: PANTALLA o exportar a CSV.')
    parser.add_argument('tipo_cheque', choices=['EMITIDO', 'DEPOSITADO'], help='Tipo de cheque: EMITIDO o DEPOSITADO.')
    parser.add_argument('--estado', type=str, help='Estado del cheque (PENDIENTE, APROBADO, RECHAZADO).', required=False)
    parser.add_argument('--fecha_inicio', type=str, help='Fecha de inicio (timestamp) para filtrar.', required=False)
    parser.add_argument('--fecha_fin', type=str, help='Fecha de fin (timestamp) para filtrar.', required=False)

    args = parser.parse_args()

    # Convertidor fecha inicio y fecha fin (opt)
    fecha_inicio = int(args.fecha_inicio) if args.fecha_inicio else None
    fecha_fin = int(args.fecha_fin) if args.fecha_fin else None

    # Procesamiento de cheques con parametros.
    procesar_cheques(args.archivo_csv, args.dni, args.salida, args.tipo_cheque, args.estado, fecha_inicio, fecha_fin)

if __name__ == '__main__':
    main()
