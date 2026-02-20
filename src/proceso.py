import pathlib
import pandas as pd
import numpy as np
import openpyxl
from datetime import datetime

# 1. Descarga del Archivo de Datos
dir = pathlib.Path(__file__).resolve().parent.parent
ruta_archivo = dir / "Insumos" / "datos_ventas.xlsx"


# 2. Procesamiento de datos
def leer_datos(ruta_archivo):
    """ Funcion que lee los datos del archivo Excel."""
    ruta = pathlib.Path(ruta_archivo)

    if not ruta.exists():
        raise FileNotFoundError(f"No se encontró el archivo: {ruta}")

    return pd.read_excel(ruta)


def limpiar_datos(df_ventas):
    """ Funcion que normaliza los datos del excel, reemplazando valores nulos y cambiando el tipo de dato de fecha """

    df_ventas["Total_Venta"] = df_ventas["Total_Venta"].fillna(df_ventas["Cantidad"] * df_ventas["Precio_Unitario"])
    df_ventas["Fecha"] = pd.to_datetime(df_ventas["Fecha"])
    return df_ventas

def filtrar_ventas(df_ventas):
    """ Funcion que filtra las ventas del año 2023 """
    return df_ventas[df_ventas["Fecha"].dt.year == 2023]
