print("Arguementos por defecto")
def menu(*plato):
    
    print("Menu del dia", end=": ")
    for i in plato:
        print(i, end=" ")

menu("Pasta", "Pizza", "Ensalada", "Sopa")