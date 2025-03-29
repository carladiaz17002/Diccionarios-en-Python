# Crear el diccionario con información personal
informacion_personal = {
    "nombre": "Carlos Pérez",
    "edad": 30,
    "ciudad": "Madrid",
    "profesion": "Ingeniero"
}
# Acceder y modificar el valor de la clave "ciudad"
informacion_personal["ciudad"] = "Barcelona"

# Agregar una nueva clave-valor (ejemplo: la empresa donde trabaja)
informacion_personal["empresa"] = "Tech Solutions"
# Verificar si la clave "telefono" existe y agregarla si no está
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "123-456-7890"
# Eliminar la clave "edad"
del informacion_personal["edad"]
# Imprimir el diccionario final
print("Diccionario final:", informacion_personal)
git