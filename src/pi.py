#!/usr/bin/env python

"""Función SumRiemann implementa la suma
de Riemann para calcular una integral, donde se utiliza
el valor de la mitad del intervalo.
Toma como entradas a el punto inicial,
b el punto final, n la catidad de divisiones,
y f como la función por integrar.
"""
def SumRiemann(a,b,n,f):
    x=(b-a)/n
    x0=x/2
    res=0
    for i in range(n):
        x_f=x0+i*x
        f_x=f(x_f)
        res+=x*f_x
    return res

""" Función para el calculo de las imagenes de
la funcion fun=4/(1+xf*xf). Toma como entrada
el valor de la preimagen.
"""
def Funcion_Matematica(xf):
    fun=4/(1+xf*xf)
    return fun

"Se invoca la función SumRiemann, sustituyendo las variables (a,b,n,f) respectivamente"
A=0
B=1
N=1000
Resultado=SumRiemann(A,B,N,Funcion_Matematica)
print(Resultado)
