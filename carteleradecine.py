peliculas = ["Avatar", "Titanic", "Interestelar"]
salas = ["Sala 1", "Sala 2", "Sala 3"]

if "Interestelar" in peliculas:
    peliculas.append("Duna")
else:
    print("esta string no esta en la lista")
    
if "Sala 3" in salas:
    salas.append("Sala VIP")
    
if "Titanic" in peliculas:
    peliculas.remove("Titanic")
    
if len(salas) > 3:
    salas.pop(0)
    
if "Avatar" in peliculas:
    peliculas.remove("Avatar")
    peliculas.append("Avatar 2")
    
estrenos = peliculas[:2]
salas_disponibles = salas[-2:]

if "Sala VIP" in salas_disponibles:
    funcion_especial = ("Duna", "Sala VIP")

if "Avatar 2" in estrenos:
    estrenos.append("3D")

if "3D" in estrenos:
    programacion = {"pelicula": "Avatar 2", "sala": "Sala 2", "formato": "3D"}
    
if 'programacion' in locals():
    programacion["hora"] = "6:30PM"

if "Sala 4" not in salas:
    salas.append("Sala 4")

if "Titanic" not in peliculas:
    peliculas.append("Titanic")
    


print(salas)
print(peliculas)
print(estrenos)
print(salas_disponibles)
print(funcion_especial)

if 'programacion' in locals():
    print(programacion)


