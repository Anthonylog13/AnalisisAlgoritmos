import sympy as sp
from math import *
def biseccion():
    solucion = None
    contador = 0
    error_calculado = 101
    x = sp.Symbol('x')
    g_str = input('Digite la funcion: ')
    funcion = sp.sympify(g_str)
    g = sp.lambdify(x, funcion)
    x_i = float(input('Digite un valor inicial: '))
    x_f = float(input('Digite un valor final: '))
    iteraciones = int(input('Digite las iteraciones a realizar: '))
    tolerancia = float(input('Digite el error maximo permitido: '))
    if funcion.subs(x, x_i) * funcion.subs(x, x_f) <= 0: 
        while contador <= iteraciones and error_calculado >= tolerancia:
            contador += 1
            solucion = (x_i + x_f) / 2
            error_calculado = abs((solucion - x_i) / solucion) * 100
            if funcion.subs(x, x_i) * funcion.subs(x, solucion) >= 0:
                x_i = solucion
            else:
                x_f = solucion   
        print('La solucion es:', solucion)
        print('Encontrada en:', contador, 'iteraciones') 
        print('Con un error relativo de:{:.2f}'.format(error_calculado) + '%')
    else:
        print('No existe solucion en ese intervalo')
        

def newton_raphson():
    x = sp.Symbol('x')
    f= input('Digite la funcion(con variable x): ')

    x_ini = float(input('Digite un valor inicial: '))
    
    
    tolerancia = float(input('Digite el error maximo permitido: '))
    iteraciones = int(input('Digite las iteraciones a realizar: '))
    
    df=sp.diff(f)
    f=sp.lambdify(x,f)
    df=sp.lambdify(x,df)
    for k in range(iteraciones):
        x1= x_ini - f(x_ini)/df(x_ini)
        if(abs(x1-x_ini)<tolerancia):
            print('x',k+1, '=', x1, end='' )
            print('es una buena aproximacion de la raiz')
            return
        x_ini=x1
        print('x', k+1, '=', x1)


def punto_fijo():
    x = sp.Symbol('x')
    g_str = input('Digite la funcion: ')
    g_expr = sp.sympify(g_str)
    g = sp.lambdify(x, g_expr) 
    x_ini = float(input('Digite un valor inicial: '))
    tolerancia = float(input('Digite el error maximo permitido: '))
    iteraciones = int(input('Digite las iteraciones a realizar: '))
    
    
    g_derivada = sp.diff(g_expr, x)
    
    
    g_func = sp.lambdify(x, g_expr, 'numpy')
    g_derivada_func = sp.lambdify(x, g_derivada, 'numpy')
    
    
    if abs(g_derivada_func(x_ini)) > 1:
        print("Elegiste una funcioón que no converge") 
        return 
    else:
        print("Oh sí :)")
        sol = [x_ini]
        for i in range(iteraciones):
            sol.append(g_func(sol[-1]))
            error = abs((sol[-1] - sol[-2]) / sol[-1])
            
            if error < tolerancia:
                print("Iteración:", i+1)
                print("Solución:", sol[-1])
                print("Error:", error)
                return sol[-1]
        
        print("Iteración:", iteraciones)
        print("Solución:", sol[-1])
        print("Error:", error)
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