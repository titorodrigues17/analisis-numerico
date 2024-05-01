import numpy as np  # Importar numpy para manejo de arreglos y funciones matemáticas
import matplotlib.pyplot as plt  # Importar matplotlib para graficación de datos
from scipy.interpolate import CubicSpline  # Importar la clase CubicSpline de scipy.interpolate para generar splines cúbicas 

# Datos del Cuadro 1
x = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10] # Valores de x
y = [2.5, 2.8, 3, 3.3, 3.8, 4.8, 4.8, 5, 4.8, 4.7, 4.7, 4.5, 4.5, 4.4, 4.3, 4.4, 4.2, 4, 4.1, 4.3, 3.5] # Valores de y

# Crear el objeto de spline cúbica
spline = CubicSpline(x, y) # Generar la spline cúbica 

# Generar 200 puntos entre 0 y 10 para la graficación
xi = np.linspace(0, 10, 200) # Valores de x para la spline cúbica, la funcion linspace genera 200 puntos entre 0 y 10
yi_spline = spline(xi) # Evaluar la spline cúbica en los valores de x generados

# Graficar los puntos dados y la spline cúbica
plt.figure(figsize=(10, 6))  # Tamaño de la figura en pulgadas (ancho, alto)
plt.plot(x, y, 'o', label='Datos del Cuadro 1')  # Graficar los puntos dados con círculos (o)
plt.plot(xi, yi_spline, '-', label='Spline cúbica') # Graficar la spline cúbica con una línea sólida (-)
plt.xlabel('x') # Etiqueta del eje x 
plt.ylabel('y') # Etiqueta del eje y
plt.title('Spline cúbica') # Título de la gráfica 

plt.legend() # Mostrar la leyenda de la gráfica 
plt.grid(True) # Mostrar la cuadrícula en la gráfica
plt.show() # Mostrar la gráfica