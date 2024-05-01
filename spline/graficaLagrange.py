from sympy import symbols, lambdify # Importar las funciones symbols y lambdify de la librería sympy para cálculo simbólico y evaluación numérica
import numpy as np  # Importar numpy para manejo de arreglos y funciones matemáticas
import matplotlib.pyplot as plt # Importar matplotlib para graficación de datos

# Define la función para evaluar el polinomio de Lagrange
x = symbols('x') # Definir el símbolo x para la variable independiente
lagrange_poly = 3.31196134793712e-9 * x**20 - 3.18592028076298e-7 * x**19 + 1.41858262133535e-5 * x**18 - 0.000387870508837354 * x**17 + 0.007284068667631 * x**16 - 0.0995506543753333 * x**15 + 1.02335052847936 * x**14 - 8.06285562170062 * x**13 + 49.1393417627061 * x**12 - 231.964406970031 * x**11 + 842.528254813441 * x**10 - 2315.09386864132 * x**9 + 4649.71636410022 * x**8 - 6328.00955315269 * x**7 + 4584.56891758079 * x**6 + 1113.59350132749 * x**5 - 6347.67571679763 * x**4 + 6439.58630502099 * x**3 - 2980.40781026245 * x**2 + 531.650816899977 * x + 2.5
lagrange_func = lambdify(x, lagrange_poly) # Convertir el polinomio de Lagrange a una función numérica

# Datos de las estaciones
points = [(0, 2.5), (0.5, 2.8), (1, 3), (1.5, 3.3), (2, 3.8), (2.5, 4.8), (3, 4.8), (3.5, 5), (4, 4.8), (4.5, 4.7),
          (5, 4.7), (5.5, 4.5), (6, 4.5), (6.5, 4.4), (7, 4.3), (7.5, 4.4), (8, 4.2), (8.5, 4), (9, 4.1), (9.5, 4.3), (10, 3.5)]

# Crea un conjunto de puntos para evaluar el polinomio de Lagrange
x_values = np.linspace(0, 10, 200) # Valores de x para evaluar el polinomio de Lagrange
y_values = lagrange_func(x_values) # Evaluar el polinomio de Lagrange en los valores de x

# Grafica los puntos y el polinomio de Lagrange
plt.figure(figsize=(8, 6)) # Tamaño de la figura en pulgadas (ancho, alto)
plt.plot(x_values, y_values, label='Polinomio de Lagrange', color='blue') # Graficar el polinomio de Lagrange
plt.scatter([point[0] for point in points], [point[1] for point in points], color='red', label='Puntos') # Graficar los puntos
plt.xlabel('x') # Etiqueta del eje x
plt.ylabel('y') # Etiqueta del eje y
plt.title('Polinomio de Lagrange y Puntos') # Título de la gráfica
plt.legend() # Mostrar la leyenda
plt.grid(True) # Mostrar la cuadrícula
plt.show() # Mostrar la gráfica
