import sympy as sp
import time
from memory_profiler import profile



@profile
def biseccion():
    solucion = None
    contador = 0
    error_calculado = 101
    x = sp.Symbol('x')
    g_str = input('Digite la función: ')
    funcion = sp.sympify(g_str)
    g = sp.lambdify(x, funcion)
    x_i = float(input('Digite un valor inicial: '))
    x_f = float(input('Digite un valor final: '))
    iteraciones = int(input('Digite las iteraciones a realizar: '))
    tolerancia = float(input('Digite el error máximo permitido: '))
    
    if funcion.subs(x, x_i) * funcion.subs(x, x_f) <= 0: 
        start_time = time.time()  # Registra el tiempo de inicio
        while contador <= iteraciones and error_calculado >= tolerancia:
            contador += 1
            solucion = (x_i + x_f) / 2
            error_calculado = abs((solucion - x_i) / solucion) * 100
            if funcion.subs(x, x_i) * funcion.subs(x, solucion) >= 0:
                x_i = solucion
            else:
                x_f = solucion   
        end_time = time.time()  # Registra el tiempo de finalización
        execution_time = end_time - start_time  # Calcula el tiempo de ejecución
        
        print('La solución es:', solucion)
        print('Encontrada en:', contador, 'iteraciones') 
        print('Con un error relativo de: {:.2f}%'.format(error_calculado))
        print('Tiempo de ejecución: {:.6f} segundos'.format(execution_time))
    else:
        print('No existe solución en ese intervalo')

        
        
        
        
        
        
        
@profile
def newton_raphson():
    x = sp.Symbol('x')
    f_str = input('Digite la función (con variable x): ')
    x_ini = float(input('Digite un valor inicial: '))
    tolerancia = float(input('Digite el error máximo permitido: '))
    iteraciones = int(input('Digite las iteraciones a realizar: '))
    
    f = sp.sympify(f_str)
    df = sp.diff(f)
    f_func = sp.lambdify(x, f)
    df_func = sp.lambdify(x, df)
    
    start_time = time.time()  # Registra el tiempo de inicio
    
    for k in range(iteraciones):
        x1 = x_ini - f_func(x_ini) / df_func(x_ini)
        if abs(x1 - x_ini) < tolerancia:
            print('La raíz aproximada es:', x1)
            print('Encontrada en', k + 1, 'iteraciones')
            print('Con un error de', abs(x1 - x_ini))
            end_time = time.time()  # Registra el tiempo de finalización
            execution_time = end_time - start_time  # Calcula el tiempo de ejecución
            print('Tiempo de ejecución:', execution_time, 'segundos')
            return
        x_ini = x1
        print('x', k + 1, '=', x1)

    end_time = time.time()  # Registra el tiempo de finalización
    execution_time = end_time - start_time  # Calcula el tiempo de ejecución
    print('No se ha encontrado una raíz en', iteraciones, 'iteraciones')
    print('Tiempo de ejecución:', execution_time, 'segundos')

@profile
def punto_fijo():
    x = sp.Symbol('x')
    g_str = input('Digite la función: ')
    g_expr = sp.sympify(g_str)
    g = sp.lambdify(x, g_expr) 
    x_ini = float(input('Digite un valor inicial: '))
    tolerancia = float(input('Digite el error máximo permitido: '))
    iteraciones = int(input('Digite las iteraciones a realizar: '))
    
    g_derivada = sp.diff(g_expr, x)
    
    g_func = sp.lambdify(x, g_expr, 'numpy')
    g_derivada_func = sp.lambdify(x, g_derivada, 'numpy')
    
    if abs(g_derivada_func(x_ini)) > 1:
        print("La función elegida no converge") 
        return 
    else:
        start_time = time.time()  # Registra el tiempo de inicio
        sol = [x_ini]
        for i in range(iteraciones):
            sol.append(g_func(sol[-1]))
            error = abs((sol[-1] - sol[-2]) / sol[-1])
            
            if error < tolerancia:
                print("Iteración:", i+1)
                print("Solución:", sol[-1])
                print("Error:", error)
                break
        
        end_time = time.time()  # Registra el tiempo de finalización
        execution_time = end_time - start_time  # Calcula el tiempo de ejecución
        print("Tiempo de ejecución:", execution_time, "segundos")
        return sol[-1]

def menu():
    while True:
        print("\nSeleccione el método que desea utilizar:")
        print("1. Bisección")
        print("2. Newton-Raphson")
        print("3. Punto Fijo")
        print("4. Salir")
        
        opcion = input("Ingrese el número correspondiente a su elección: ")
        
        if opcion == "1":
            biseccion()
        elif opcion == "2":
            newton_raphson()
        elif opcion == "3":
            punto_fijo()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 4.")


menu()