from sympy import symbols, simplify # Importar las funciones symbols y simplify de la librería sympy para cálculo simbólico y simplificación de expresiones

def lagrange_polynomial_symbolic(points): # Función para calcular el polinomio de Lagrange simbólicamente
    """
    Encuentra el polinomio de Lagrange simbólicamente
    :param points: Lista de tuplas (x, y) que representan los puntos conocidos
    :return: Polinomio de Lagrange
    """
    x = symbols('x') # Definir el símbolo x para la variable independiente
    n = len(points) # Número de puntos
    polynomial = 0 # Inicializar el polinomio de Lagrange

    for i in range(n): # Iterar sobre los puntos
        term = points[i][1] # Inicializar el término del polinomio
        for j in range(n): # Iterar sobre los puntos
            if j != i: # Si j es diferente de i
                term *= (x - points[j][0]) / (points[i][0] - points[j][0]) # Calcular el término del polinomio de Lagrange
        polynomial += term # Agregar el término al polinomio

    return simplify(polynomial) # Simplificar y devolver el polinomio de Lagrange

# Datos de las estaciones
points = [(0, 2.5), (0.5, 2.8), (1, 3), (1.5, 3.3), (2, 3.8), (2.5, 4.8), (3, 4.8), (3.5, 5), (4, 4.8), (4.5, 4.7), 
          (5, 4.7), (5.5, 4.5), (6, 4.5), (6.5, 4.4), (7, 4.3), (7.5, 4.4), (8, 4.2), (8.5, 4), (9, 4.1), (9.5, 4.3), (10, 3.5)]

# Encuentra el polinomio de Lagrange
lagrange_poly = lagrange_polynomial_symbolic(points)  # Calcular el polinomio de Lagrange
print("El polinomio de Lagrange es:") # Imprimir el mensaje
print(lagrange_poly) # Imprimir el polinomio de Lagrange

