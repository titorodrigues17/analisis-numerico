import numpy as np
import matplotlib.pyplot as plt

def spline_cubica(x):
    if x <= 0.5:
        return -0.273606092552671 * x**3 + 0.668401523138167 * x**2 + 2.5
    elif x <= 1:
        return 0.568030462763359 * x**3 - 1.26245483297405 * x**2 + 1.29962893962519 * x + 2.39479543
    elif x <= 1.5:
        return -0.39851575850077 * x**3 + 1.63718383081834 * x**2 - 1.6000097241672 * x + 3.36134165
    elif x <= 2:
        return 1.82603257123973 * x**3 - 8.37328365301389 * x**2 + 13.4156915015812 * x - 4.146508961
    elif x <= 2.5:
        return -4.50561452645814 * x**3 + 29.6165989331733 * x**2 - 62.5640736707932 * x + 46.5066678
    elif x <= 3:
        return 4.19642553459282 * x**3 - 35.6487015247089 * x**2 + 100.599177473912 * x - 89.46270813
    elif x <= 3.5:
        return -2.68008761191315 * x**3 + 26.2399167938449 * x**2 - 85.0666774817491 * x + 96.2031468
    elif x <= 4:
        return 1.72392491305979 * x**3 - 20.0022147183711 * x**2 + 76.7807828110067 * x - 92.61889018
    elif x <= 4.5:
        return -0.215612040326006 * x**3 + 3.27222872225853 * x**2 - 16.3169909515116 * x + 31.511474
    elif x <= 5:
        return -0.861476751755774 * x**3 + 11.9914023265604 * x**2 - 55.55327217087 * x + 90.3658966
    elif x <= 5.5:
        return 1.2615190473491 * x**3 - 19.8535346600128 * x**2 + 103.671412761996 * x - 175.0085782
    elif x <= 6:
        return -0.984599437640634 * x**3 + 17.2074203423179 * x**2 - 100.163839750823 * x + 198.68938
    elif x <= 6.5:
        return 0.276878703213436 * x**3 - 5.49918619305536 * x**2 + 36.0757994614167 * x - 73.7898937
    elif x <= 7:
        return 0.677084624786881 * x**3 - 13.3032016637375 * x**2 + 86.8019000208508 * x - 183.696444
    elif x <= 7.5:
        return -1.38521720236094 * x**3 + 30.0051367063668 * x**2 - 216.356468569879 * x + 523.673081
    elif x <= 8:
        return 0.863784184656877 * x**3 - 20.5973945015342 * x**2 + 163.162515489378 * x - 425.124378
    elif x <= 8.5:
        return 0.330080463733439 * x**3 - 7.78850519937169 * x**2 + 60.6914010720778 * x - 151.868073
    elif x <= 9:
        return 0.215893960409363 * x**3 - 4.87674936460774 * x**2 + 35.9414764765843 * x - 81.7432868
    elif x <= 9.5:
        return -2.79365630537089 * x**3 + 76.381107811459 * x**2 - 695.379238108016 * x + 2112.21885
    else:
        return 2.15873126107418 * x**3 - 64.7619378322253 * x**2 + 645.479695506985 * x - 2133.834432

def simpson_compuesto_general(f, nodos):
    """
    Aproxima la integral de una función dada usando el método de Simpson compuesto generalizado.
    
    Args:
    - f: La función a integrar.
    - nodos: Lista de nodos donde se evaluará la función.
    
    Returns:
    - Aproximación de la integral usando el método de Simpson compuesto.
    """
    h = nodos[1] - nodos[0]  # Calcular el ancho de los subintervalos
    suma = 0
    for i in range(0, len(nodos) - 2, 2):
        suma += f(nodos[i]) + 4 * f(nodos[i+1]) + f(nodos[i+2])
    return h * suma / 3

# Rango de valores para x
x_values = np.linspace(0, 10, 1000)

# Evaluar la función en cada punto de x
y_values = [spline_cubica(x) for x in x_values]

# Graficar la función y el área bajo la curva
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='Spline Cúbica', color='blue')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfica de la Spline Cúbica y Área bajo la Curva con Simpson')

# Calcular y graficar el área bajo la curva
area_x = np.linspace(0, 10, 100)
area_y = [spline_cubica(x) for x in area_x]
plt.fill_between(area_x, area_y, color='skyblue', alpha=0.4, label='Área bajo la curva')

plt.grid(True)
plt.legend()
plt.show()

# Calcular la aproximación de la integral usando el método de Simpson compuesto
resultado = simpson_compuesto_general(spline_cubica, x_values)
print("Aproximación de la integral usando Simpson:", resultado)
