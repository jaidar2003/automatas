import datetime


import datetime

usuarios = [
    {"id": 1, "nombre": "Napoleon Bonaparte", "conexiones": [
        {"fecha": datetime.date(2020, 3, 15), "duracion": 120},
        {"fecha": datetime.date(2020, 4, 20), "duracion": 200},
    ]},
    {"id": 2, "nombre": "Sofia SOler", "conexiones": [
        {"fecha": datetime.date(2020, 3, 25), "duracion": 300},
        {"fecha": datetime.date(2020, 5, 30), "duracion": 150},
    ]},
    {"id": 3, "nombre": "Juan Manuel Aidar", "conexiones": [
        {"fecha": datetime.date(2020, 2, 14), "duracion": 180},
        {"fecha": datetime.date(2020, 3, 18), "duracion": 160},
    ]},
    {"id": 4, "nombre": "Julius Caesar", "conexiones": [
        {"fecha": datetime.date(2020, 1, 10), "duracion": 250},
        {"fecha": datetime.date(2020, 2, 22), "duracion": 100},
    ]},
    {"id": 5, "nombre": "Genghis Khan", "conexiones": [
        {"fecha": datetime.date(2020, 6, 5), "duracion": 220},
        {"fecha": datetime.date(2020, 7, 8), "duracion": 300},
    ]},
    {"id": 6, "nombre": "Leonardo da Vinci", "conexiones": [
        {"fecha": datetime.date(2020, 8, 13), "duracion": 90},
        {"fecha": datetime.date(2020, 9, 17), "duracion": 210},
    ]},
    {"id": 7, "nombre": "Galileo Galilei", "conexiones": [
        {"fecha": datetime.date(2020, 10, 12), "duracion": 140},
        {"fecha": datetime.date(2020, 11, 15), "duracion": 170},
    ]},
    {"id": 8, "nombre": "Marie Curie", "conexiones": [
        {"fecha": datetime.date(2020, 12, 1), "duracion": 260},
        {"fecha": datetime.date(2021, 1, 5), "duracion": 180},
    ]},
    {"id": 9, "nombre": "Albert Einstein", "conexiones": [
        {"fecha": datetime.date(2021, 2, 14), "duracion": 300},
        {"fecha": datetime.date(2021, 3, 18), "duracion": 150},
    ]},
    {"id": 10, "nombre": "Isaac Newton", "conexiones": [
        {"fecha": datetime.date(2021, 4, 10), "duracion": 240},
        {"fecha": datetime.date(2021, 5, 22), "duracion": 160},
    ]},
    {"id": 11, "nombre": "Socrates", "conexiones": [
        {"fecha": datetime.date(2021, 6, 5), "duracion": 120},
        {"fecha": datetime.date(2021, 7, 8), "duracion": 180},
    ]},
    {"id": 12, "nombre": "Mauricio Macri", "conexiones": [
        {"fecha": datetime.date(2021, 8, 13), "duracion": 210},
        {"fecha": datetime.date(2021, 9, 17), "duracion": 230},
    ]},
    {"id": 13, "nombre": "Aristoteles", "conexiones": [
        {"fecha": datetime.date(2021, 10, 12), "duracion": 130},
        {"fecha": datetime.date(2021, 11, 15), "duracion": 170},
    ]},
    {"id": 14, "nombre": "William Shakespeare", "conexiones": [
        {"fecha": datetime.date(2021, 12, 1), "duracion": 300},
        {"fecha": datetime.date(2022, 1, 5), "duracion": 90},
    ]},
    {"id": 15, "nombre": "Cristobal Colon", "conexiones": [
        {"fecha": datetime.date(2022, 2, 14), "duracion": 270},
        {"fecha": datetime.date(2022, 3, 18), "duracion": 120},
    ]},
    {"id": 16, "nombre": "Dino Meschini", "conexiones": [
        {"fecha": datetime.date(2022, 4, 10), "duracion": 230},
        {"fecha": datetime.date(2022, 5, 22), "duracion": 140},
    ]},
    {"id": 17, "nombre": "San Martin", "conexiones": [
        {"fecha": datetime.date(2022, 6, 5), "duracion": 210},
        {"fecha": datetime.date(2022, 7, 8), "duracion": 160},
    ]},
    {"id": 18, "nombre": "Manuel Belgrano", "conexiones": [
        {"fecha": datetime.date(2022, 8, 13), "duracion": 180},
        {"fecha": datetime.date(2022, 9, 17), "duracion": 200},
    ]},
    {"id": 19, "nombre": "Benjamin Franklin", "conexiones": [
        {"fecha": datetime.date(2022, 10, 12), "duracion": 150},
        {"fecha": datetime.date(2022, 11, 15), "duracion": 190},
    ]},
    {"id": 20, "nombre": "Mahatma Gandhi", "conexiones": [
        {"fecha": datetime.date(2022, 12, 1), "duracion": 300},
        {"fecha": datetime.date(2023, 1, 5), "duracion": 100},
    ]},
    {"id": 21, "nombre": "Nelson Mandela", "conexiones": [
        {"fecha": datetime.date(2023, 2, 14), "duracion": 270},
        {"fecha": datetime.date(2023, 3, 18), "duracion": 150},
    ]},
    {"id": 22, "nombre": "Martin Luther King Jr.", "conexiones": [
        {"fecha": datetime.date(2023, 4, 10), "duracion": 230},
        {"fecha": datetime.date(2023, 5, 22), "duracion": 170},
    ]},
    {"id": 23, "nombre": "Mother Teresa", "conexiones": [
        {"fecha": datetime.date(2023, 6, 5), "duracion": 210},
        {"fecha": datetime.date(2023, 7, 8), "duracion": 160},
    ]},
    {"id": 24, "nombre": "Juana de Arco", "conexiones": [
        {"fecha": datetime.date(2023, 8, 13), "duracion": 180},
        {"fecha": datetime.date(2023, 9, 17), "duracion": 190},
    ]},
    {"id": 25, "nombre": "Reina Victoria", "conexiones": [
        {"fecha": datetime.date(2023, 10, 12), "duracion": 150},
        {"fecha": datetime.date(2023, 11, 15), "duracion": 210},
    ]},
    {"id": 26, "nombre": "Winston Churchill", "conexiones": [
        {"fecha": datetime.date(2023, 12, 1), "duracion": 300},
        {"fecha": datetime.date(2024, 1, 5), "duracion": 130},
    ]},
    {"id": 27, "nombre": "Franklin D. Roosevelt", "conexiones": [
        {"fecha": datetime.date(2024, 2, 14), "duracion": 270},
        {"fecha": datetime.date(2024, 3, 18), "duracion": 150},
    ]},
    {"id": 28, "nombre": "Margaret Thatcher", "conexiones": [
        {"fecha": datetime.date(2024, 4, 10), "duracion": 230},
        {"fecha": datetime.date(2024, 5, 22), "duracion": 170},
    ]},
    {"id": 29, "nombre": "Leon Trotsky", "conexiones": [
        {"fecha": datetime.date(2024, 6, 5), "duracion": 210},
        {"fecha": datetime.date(2024, 6, 12), "duracion": 160},
    ]},
]


def filtrar_usuarios_por_fecha(usuarios, fecha_inicio, fecha_fin):
    usuarios_filtrados = []
    for usuario in usuarios:
        total_duracion = 0
        for conexion in usuario["conexiones"]:
            if fecha_inicio <= conexion["fecha"] <= fecha_fin:
                total_duracion += conexion["duracion"]
        if total_duracion > 0:
            usuarios_filtrados.append(
                {"id": usuario["id"], "nombre": usuario["nombre"], "total_duracion": total_duracion})

    # Ordenar por duración de conexión en forma descendente
    usuarios_filtrados.sort(key=lambda x: x["total_duracion"], reverse=True)

    return usuarios_filtrados


# Ejemplo de uso
fecha_inicio = datetime.date(2020, 3, 1)
fecha_fin = datetime.date(2021, 3, 31)

usuarios_filtrados = filtrar_usuarios_por_fecha(usuarios, fecha_inicio, fecha_fin)
for usuario in usuarios_filtrados:
    print(f"ID: {usuario['id']}, Nombre: {usuario['nombre']}, Duración Total: {usuario['total_duracion']} minutos")
import tkinter as tk
from tkinter import ttk


# Función para mostrar usuarios filtrados
def mostrar_usuarios():
    fecha_inicio = datetime.datetime.strptime(entry_fecha_inicio.get(), "%Y-%m-%d").date()
    fecha_fin = datetime.datetime.strptime(entry_fecha_fin.get(), "%Y-%m-%d").date()

    usuarios_filtrados = filtrar_usuarios_por_fecha(usuarios, fecha_inicio, fecha_fin)

    # Limpiar el Treeview
    for row in tree.get_children():
        tree.delete(row)

    # Insertar los datos filtrados
    for usuario in usuarios_filtrados:
        tree.insert("", "end", values=(usuario["id"], usuario["nombre"], usuario["total_duracion"]))


# Configuración de la ventana principal
root = tk.Tk()
root.title("Seguimiento de Usuarios")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Entrada de fecha de inicio
ttk.Label(frame, text="Fecha Inicio (YYYY-MM-DD):").grid(row=0, column=0, padx=5, pady=5)
entry_fecha_inicio = ttk.Entry(frame)
entry_fecha_inicio.grid(row=0, column=1, padx=5, pady=5)

# Entrada de fecha de fin
ttk.Label(frame, text="Fecha Fin (YYYY-MM-DD):").grid(row=1, column=0, padx=5, pady=5)
entry_fecha_fin = ttk.Entry(frame)
entry_fecha_fin.grid(row=1, column=1, padx=5, pady=5)

# Botón para mostrar usuarios
btn_mostrar = ttk.Button(frame, text="Mostrar Usuarios", command=mostrar_usuarios)
btn_mostrar.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Treeview para mostrar los usuarios filtrados
tree = ttk.Treeview(frame, columns=("id", "nombre", "duracion"), show="headings")
tree.heading("id", text="ID")
tree.heading("nombre", text="Nombre")
tree.heading("duracion", text="Duración Total")
tree.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Iniciar la aplicación
root.mainloop()