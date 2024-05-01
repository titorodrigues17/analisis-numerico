import numpy as np
import matplotlib.pyplot as plt

def trapecio_compuesto_general(f, nodos):
    
    h = nodos[1] - nodos[0]  # Calcular el ancho de los subintervalos
    suma = 0
    for i in range(len(nodos) - 1):
        suma += (f(nodos[i]) + f(nodos[i+1])) / 2

# Definir la función dada
def funcion(x):
    return 3.31196134793712e-9 * x**20 - 3.18592028076298e-7 * x**19 + 1.41858262133535e-5 * x**18 - 0.000387870508837354 * x**17 + 0.007284068667631 * x**16 - 0.0995506543753333 * x**15 + 1.02335052847936 * x**14 - 8.06285562170062 * x**13 + 49.1393417627061 * x**12 - 231.964406970031 * x**11 + 842.528254813441 * x**10 - 2315.09386864132 * x**9 + 4649.71636410022 * x**8 - 6328.00955315269 * x**7 + 4584.56891758079 * x**6 + 1113.59350132749 * x**5 - 6347.67571679763 * x**4 + 6439.58630502099 * x**3 - 2980.40781026245 * x**2 + 531.650816899977 * x + 2.5

# Definir los puntos dados
x = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10])

# Calcular la aproximación de la integral usando el método del trapecio compuesto
resultado = trapecio_compuesto_general(funcion, x)
print("Aproximación de la integral usando trapecio:", resultado)

# Crear una gráfica de la función y el área aproximada bajo la curva
x_vals = np.linspace(min(x), max(x), 100)
y_vals = funcion(x_vals)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='Función dada')
plt.scatter(x, funcion(x), color='red', label='Puntos')
plt.fill_between(x_vals, y_vals, color='skyblue', alpha=0.4, label='Área aproximada')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Área aproximada bajo la curva y puntos dados usando trapecio compuesto')
plt.legend()
plt.grid(True)
plt.show()
