def contar(count=1):
    print(count)
    if count < 10:
        return contar(count+1) 

contar()