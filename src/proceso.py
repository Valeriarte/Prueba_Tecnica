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


def agregar_mes(df_ventas):
    """ Funcion que agrega la columna de mes a las ventas"""
    df_ventas["Mes"] = df_ventas["Fecha"].dt.month
    return df_ventas


def calcular_resumen(df_ventas):
    """ Funcion que calcula el resumen de ventas por vendedor y mes """
    return df_ventas.groupby(["Vendedor", "Mes"])["Total_Venta"].sum().reset_index()


# 3. Generación de Reporte
def resumen_ventas(resumen_vendedor_mes):
    """ Funcion que genera un archivo Excel con el resumen de ventas """
    nombre_archivo = datetime.now().strftime("resumen_ventas_2023_%H%M%S.xlsx")
    ventas_por_mes = resumen_vendedor_mes.groupby("Mes")["Total_Venta"].sum().reset_index()

    with pd.ExcelWriter(nombre_archivo, engine="openpyxl") as writer:
        resumen_vendedor_mes.to_excel(writer, sheet_name="Ventas_por_Vendedor_y_Mes", index=False)
        ventas_por_mes.to_excel(writer, sheet_name="Ventas_por_Mes", index=False)

    print(f"Archivo final: {nombre_archivo}")