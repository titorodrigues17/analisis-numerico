import sympy as sp  # Importar la librería sympy para cálculo simbólico y álgebra computacional

def spline_cubica_natural(x, y, xi):  # Función para calcular la spline cúbica (x: valores de x, y: valores de y, xi: variable independiente)
    """
    Calcula la spline cúbica natural simbólicamente.

    Args:
    x: Lista de valores x.
    y: Lista de valores y correspondientes a los valores x.
    xi: El símbolo de la variable independiente.

    Returns:
    El polinomio de la spline cúbica natural simbólico.
    """
    n = len(x) # Número de puntos
    h = [x[i] - x[i-1] for i in range(1, n)]  # Distancias entre los puntos x
    alpha = [0] + [3 * ((y[i+1] - y[i]) / h[i] - (y[i] - y[i-1]) / h[i-1]) for i in range(1, n-1)] + [0] # Coeficientes alpha de la spline cúbica

    A = sp.zeros(n, n) # Crear una matriz de ceros de tamaño n x n
    b = sp.zeros(n, 1) # Crear un vector columna de ceros de tamaño n x 1
    A[0, 0] = 1 # Asignar el valor 1 a la posición (0, 0) de la matriz A
    A[n-1, n-1] = 1 # Asignar el valor 1 a la posición (n-1, n-1) de la matriz A
    for i in range(1, n-1): # Iterar sobre los valores de i desde 1 hasta n-2
        A[i, i-1] = h[i-1] # Asignar el valor h[i-1] a la posición (i, i-1) de la matriz A
        A[i, i] = 2 * (h[i-1] + h[i]) # Asignar el valor 2 * (h[i-1] + h[i]) a la posición (i, i) de la matriz A
        A[i, i+1] = h[i]# Asignar el valor h[i] a la posición (i, i+1) de la matriz A
        b[i] = alpha[i] # Asignar el valor alpha[i] al elemento i del vector columna b

    c = A.inv() * b # Calcular el vector columna c de coeficientes de la spline cúbica

    # Calcular los coeficientes de los polinomios cúbicos
    a = [y[i] for i in range(n-1)] # Coeficientes a de la spline cúbica
    b = [(y[i+1] - y[i]) / h[i] - h[i] * (2 * c[i] + c[i+1]) / 3 for i in range(n-1)] # Coeficientes b de la spline cúbica
    d = [(c[i+1] - c[i]) / (3 * h[i]) for i in range(n-1)] # Coeficientes d de la spline cúbica

    # Crear el polinomio para cada tramo de la spline
    polinomios = [] # Lista para almacenar los polinomios de la spline cúbica
    for i in range(n-1): # Iterar sobre los valores de i desde 0 hasta n-2
        polinomio = a[i] + b[i] * (xi - x[i]) + c[i] * (xi - x[i])**2 + d[i] * (xi - x[i])**3   # Polinomio cúbico para el tramo i
        polinomios.append(polinomio) # Agregar el polinomio a la lista de polinomios
        #polinomios.append(polinomio.expand().simplify())  # Expandir y simplificar el polinomio

    # Definir la spline cúbica natural por partes
    spline = sp.Piecewise((polinomios[0], xi <= x[1]), *[(polinomios[i], (xi > x[i]) & (xi <= x[i+1])) for i in range(n-2)], (polinomios[-1], xi > x[-2])) # Definir la spline cúbica natural por partes

    return spline # Devolver la spline cúbica natural


# Datos del Cuadro 1

x = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10] # Valores de x
y = [2.5, 2.8, 3, 3.3, 3.8, 4.8, 4.8, 5, 4.8, 4.7, 4.7, 4.5, 4.5, 4.4, 4.3, 4.4, 4.2, 4, 4.1, 4.3, 3.5] # Valores de y
X = sp.symbols('X') # Definir el símbolo X para la variable independiente
spline = spline_cubica_natural(x, y, X) # Calcular la spline cúbica natural simbólicamente
spline = sp.expand(spline) # Expandir la spline cúbica
spline = sp.simplify(spline)    # Simplificar la spline cúbica
# Imprimir el resultado
print("La spline cúbica natural es:") # Imprimir el mensaje
#print(spline)
sp.pprint(spline, use_unicode=True) # Imprimir la spline cúbica natural, utilizando caracteres Unicode