# Prueba_Tecnica

**Autora:** Valeria Solarte Jiménez
**Fecha:** Febrero 2026

Pequeño script para leer, normalizar, filtrar y resumir ventas desde un Excel y generar un reporte en Excel.

Estructura
- Main.py                      -> Orquestador (muestra resultados en consola y genera el Excel)
- src/proceso.py               -> Funciones: leer_datos, limpiar_datos, filtrar_ventas, agregar_mes, calcular_resumen, resumen_ventas
- Insumos/datos_ventas.xlsx    -> Archivo de entrada (debe existir)
- requirements.txt             -> Dependencias del proyecto
- .venv/                       -> Virtualenv (recomendado)

Requisitos
- Python 3.8+
- Las dependencias están en requirements.txt

Instalación (Windows PowerShell)
1. Crear y activar el entorno virtual:
   ```
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
2. Instalar dependencias:
   ```
   pip install -r requirements.txt
   ```

Uso
- Asegúrate de que `Insumos/datos_ventas.xlsx` existe en la raíz del proyecto.
- Ejecutar desde la raíz del proyecto:
  ```
  python .\Main.py
  ```
  o usando el intérprete del virtualenv:
  ```
  .\.venv\Scripts\python.exe .\Main.py
  ```
- Si prefieres usar `-m`, pasa el nombre del módulo SIN la extensión `.py`:
  ```
  python -m Main
  ```

Salida
- En consola se muestran resultados intermedios (head/info) para cada paso.
- Se genera un archivo Excel con timestamp: `resumen_ventas_2023_YYYYMMDD_HHMMSS.xlsx`.

Notas / buenas prácticas
- `Main.py` actualmente añade `src` a `sys.path` para importar `proceso`. Alternativa más limpia: convertir `src` en paquete añadiendo `src/__init__.py` y cambiar imports a `from src.proceso import ...`.
- Evitar ejecutar `python -m main.py` (usar `python -m Main` o ejecutar el fichero directamente).