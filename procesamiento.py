import pandas as pd
from envio_correo import enviar_correo

def limpieza_datos(df):
    # Renombrar columnas
    df.columns = df.columns.str.lower().str.replace(' ', '_').str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    
    # Eliminar columnas repetidas
    df = df.loc[:, ~df.columns.duplicated()]
    
    # Eliminar coma de la columna "dispositivo_legal"
    df['dispositivo_legal'] = df['dispositivo_legal'].str.replace(',', '')

    return df

def dolarizar_valores(df):
    # Llamar al API de SUNAT para obtener el valor actual del dólar
    # dolar = obtener_valor_dolar_desde_api()

    # Dolarizar montos de inversión y transferencia
    # df['monto_inversion_usd'] = df['monto_inversion'] / dolar
    # df['monto_transferencia_usd'] = df['monto_transferencia'] / dolar

    return df

def puntuar_estado(df):
    estado_mapping = {'Actos Previos': 1, 'Resuelto': 0, 'Ejecucion': 2, 'Concluido': 3}
    df['estado_puntuado'] = df['estado'].map(estado_mapping)
    return df

def generar_reporte_region(df):
    regiones = df['region'].unique()
    for region in regiones:
        df_region = df[df['region'] == region]
        if not df_region.empty:
            # Generar reporte Excel con el top 5 de costo inversión por obras de tipo Urbano en estado 1, 2, 3
            reporte = df_region[(df_region['tipo_obra'] == 'Urbano') & (df_region['estado_puntuado'].isin([1, 2, 3]))].nlargest(5, 'costo_inversion')
            if not reporte.empty:
                reporte.to_excel(f'top5_costo_inversion_{region}.xlsx')
                # Envío de correo con el reporte adjunto
                enviar_correo(reporte, region)
