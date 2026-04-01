# gramos a mol

def gramos_mol():
    gramos_dados = float(input("Ingresa la cantidad de gramos que quieres convertir: "))
    gramos_sustancia = float(input("Ingresa los gramos de la sustancia que tiene en una mol: "))
    mol = gramos_dados / gramos_sustancia
    
    print(f"Estos son los gramos dados: {gramos_dados}, estos son los gramos de la sustancia en un mol: {gramos_sustancia}, y estos son los moles de la sustancia, {mol}")

# ¡AQUÍ ESTÁ EL CAMBIO! 
# Esta línea va sin espacios al principio.
gramos_mol()

