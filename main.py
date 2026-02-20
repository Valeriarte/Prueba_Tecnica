import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))
from proceso import leer_datos,limpiar_datos,filtrar_ventas,agregar_mes,calcular_resumen,resumen_ventas


def main():
    ruta = "Insumos/datos_ventas.xlsx"
   
    df=leer_datos(ruta)
    print("Datos leídos:")
    print(df.head())
    print()

    df=limpiar_datos(df)
    print("Datos normalizados:")
    df.info()
    print()

    df_2023=filtrar_ventas(df)
    print("Ventas filtradas 2023:")
    print(df_2023.head())
    print()

    df_2023=agregar_mes(df_2023)
    print("Ventas con mes agregado:")
    print(df_2023[['Fecha', 'Mes']].head())
    print()

    resumen_df=calcular_resumen(df_2023)
    print("Resumen por vendedor y mes:")
    print(resumen_df)
    print()

    resumen_ventas(resumen_df)


if __name__ == "__main__":
    main()