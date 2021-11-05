'''
Solucionador de Sudoku
Creado por José Francisco Gallardo ojeda
'''

'''Se define la variable M, correspondiente a la cantidad de filas y columnas, es decir de la matríz MxM'''
M = 9
'''Se define la tabla con las pistas entregadas, agregando 0 en las casillas no definidas.'''
tabla = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]]
def resol(cuadricula, fil, col, num):
    for x in range(M):
        if cuadricula[fil][x] == num:
            return False
    for x in range(M):
        if cuadricula[x][col] == num:
            return False
    FilInicio = fil - fil % 3
    ColInicio = col - col % 3
    for i in range(3):
        for j in range(3):
            if cuadricula[i + FilInicio][j + ColInicio] == num:
                return False
    return True

def suduko(cuadricula, fil, col):
    if (fil == M - 1 and col == M):
        return True
    if col == M:
        fil += 1
        col = 0
    if cuadricula[fil][col] > 0:
        return suduko(cuadricula, fil, col + 1)
    for num in range(1, M + 1, 1): 
        if resol(cuadricula, fil, col, num):
            cuadricula[fil][col] = num
            if suduko(cuadricula, fil, col + 1):
                return True
        cuadricula[fil][col] = 0
    return False
