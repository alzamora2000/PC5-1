from procesamiento import limpieza_datos, dolarizar_valores, puntuar_estado, generar_reporte_region
import pandas as pd

# Cargar datos desde el archivo Excel
df = pd.read_excel('data/reactiva.xlsx')

# Limpieza de datos
df = limpieza_datos(df)

# Dolarizar valores
df = dolarizar_valores(df)

# Puntuar estado
df = puntuar_estado(df)

# Generar reporte por región y enviar correo electrónico
generar_reporte_region(df)
