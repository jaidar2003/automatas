import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

file_path = os.getenv('CSV_FILE_PATH')

if not file_path:
    raise ValueError("La ruta del archivo CSV no está configurada en el archivo .env")

try:
    df = pd.read_csv(file_path, encoding='latin1', low_memory=False)
except Exception as e:
    print(f"Error al leer el archivo CSV: {e}")
    raise


df.rename(columns={
    'Inicio_de_ConexiÃ³n_Dia': 'Inicio_de_Conexión_Dia',
    'Inicio_de_ConexiÃ³n_Hora': 'Inicio_de_Conexión_Hora',
    'FIN_de_ConexiÃ³n_Dia': 'FIN_de_Conexión_Dia',
    'FIN_de_ConexiÃ³n_Hora': 'FIN_de_Conexión_Hora'
}, inplace=True)


required_columns = ['Inicio_de_Conexión_Dia', 'Inicio_de_Conexión_Hora', 'FIN_de_Conexión_Dia', 'FIN_de_Conexión_Hora']
missing_columns = [col for col in required_columns if col not in df.columns]
if missing_columns:
    raise KeyError(f"Faltan las siguientes columnas necesarias en el DataFrame: {missing_columns}")


def convertir_a_datetime_safe(df, col_dia, col_hora, new_col):
    """
    Convierte dos columnas de fecha y hora en formato string a una sola columna de tipo datetime en el DataFrame.

    Args:
    - df: DataFrame donde se encuentran las columnas.
    - col_dia: Nombre de la columna del día.
    - col_hora: Nombre de la columna de la hora.
    - new_col: Nombre de la nueva columna que se creará con el resultado de la conversión.
    """
    try:
        df[new_col] = pd.to_datetime(df[col_dia] + ' ' + df[col_hora], format='%Y-%m-%d %H:%M:%S', errors='coerce')
    except Exception as e:
        print(f"Error al convertir las columnas de fechas y horas a datetime: {e}")


convertir_a_datetime_safe(df, 'Inicio_de_Conexión_Dia', 'Inicio_de_Conexión_Hora', 'Inicio_de_Conexión')
convertir_a_datetime_safe(df, 'FIN_de_Conexión_Dia', 'FIN_de_Conexión_Hora', 'FIN_de_Conexión')


def filtrar_por_fecha(df, inicio, fin):
    """
    Filtra el DataFrame por un rango de fechas específico y ordena los resultados por Session_Time de forma descendente.

    Args:
    - df: DataFrame a filtrar.
    - inicio: Fecha de inicio del rango (datetime).
    - fin: Fecha de fin del rango (datetime).

    Returns:
    - DataFrame filtrado y ordenado por Session_Time.
    """
    mask = (df['Inicio_de_Conexión'] >= inicio) & (df['FIN_de_Conexión'] <= fin)
    df_filtrado = df.loc[mask].sort_values(by='Session_Time', ascending=False)
    return df_filtrado


def capturar_fechas():
    """
    Captura las fechas de inicio y fin del usuario por terminal.

    Returns:
    - inicio: Fecha de inicio del rango (datetime).
    - fin: Fecha de fin del rango (datetime).
    """
    try:
        inicio_str = input("Ingrese la fecha de inicio (formato YYYY-MM-DD): ")
        fin_str = input("Ingrese la fecha de fin (formato YYYY-MM-DD): ")
        inicio = pd.to_datetime(inicio_str)
        fin = pd.to_datetime(fin_str)
        return inicio, fin
    except ValueError as ve:
        print(f"Error: {ve}")
        return None, None


while True:
    inicio, fin = capturar_fechas()
    if inicio is not None and fin is not None:
        break


df_filtrado = filtrar_por_fecha(df, inicio, fin)


print("\nResultados filtrados por fecha:")
print(df_filtrado[['Usuario', 'Inicio_de_Conexión', 'FIN_de_Conexión', 'Session_Time']])
