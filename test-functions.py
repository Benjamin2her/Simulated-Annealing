from math import exp, sqrt, cos, pi, e

def rastrigin(x):
    a = 10
    sum = a*2 + x

# f(0,0) = 0; -5 <= x,y <= 5
def ackley(x, y): 
    return -20 * exp(-0.2*sqrt(0.5*(x**2 + y**2))) - exp(0.5*(cos(2*pi*x) + cos(2*pi*y))) + e + 20

def sphere(x)
    n = 3
    sum =0
    for i in range(n):
        sum += i
