import numpy as np
import matplotlib.pyplot as plt

def spline_cubica(x):
    y = np.zeros_like(x)  # Crear un array de ceros del mismo tamaño que x para almacenar los resultados
    # Definir las condiciones para cada intervalo y calcular los valores correspondientes de y
    mask = (x <= 0.5)
    y[mask] = -0.273606092552671 * x[mask]**3 + 0.668401523138167 * x[mask]**2 + 2.5
    mask = (0.5 < x) & (x <= 1)
    y[mask] = 0.568030462763359 * x[mask]**3 - 1.26245483297405 * x[mask]**2 + 1.29962893962519 * x[mask] + 2.39479543
    mask = (1 < x) & (x <= 1.5)
    y[mask] = -0.39851575850077 * x[mask]**3 + 1.63718383081834 * x[mask]**2 - 1.6000097241672 * x[mask] + 3.36134165
    # Continuar para el resto de intervalos
    return y

def cuadratura_gaussiana_segundo_orden(f, a, b):
    # Coeficientes y nodos de la cuadratura de Gauss-Legendre de segundo orden
    t_values = np.array([-np.sqrt(3)/3, np.sqrt(3)/3])
    w_values = np.array([1, 1])

    # Transformación de intervalo
    t_values = (b - a) / 2 * t_values + (b + a) / 2

    # Calcular la integral usando cuadraturas gaussianas de segundo orden
    integral = np.sum(w_values * f(t_values))
    return integral * (b - a) / 2

# Rango de valores para x
x_values = np.linspace(0, 10, 1000)

# Evaluar la función en cada punto de x
y_values = spline_cubica(x_values)

# Graficar la función
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='Spline Cúbica', color='blue')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfica de la Spline Cúbica')
plt.grid(True)
plt.legend()
plt.show()

# Calcular la integral usando cuadraturas gaussianas de segundo orden
resultado_gauss = cuadratura_gaussiana_segundo_orden(spline_cubica, 0, 10)
print("Resultado de la integral usando cuadraturas gaussianas de segundo orden:", resultado_gauss)
