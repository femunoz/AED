def salida(i,j):
    if L[i][j] == "=": # encontramos la salida
        return True
    if L[i][j] != " ": # espacio ocupado
        return False
    if salida(i,j-1) or salida(i,j+1) or salida(i-1,j) or salida(i+1,j):
        return True
    return False

L = [
"+--+-----+--+",
"|  |     |  |",
"|  +--+     =",
"|     |  |  |",
"+--+  |  |  |",
"|  |        |",
"|  |     |  |",
"+--+-----+--+"
]
print(salida(5,2))
