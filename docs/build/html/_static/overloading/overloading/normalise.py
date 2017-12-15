from fenics import *

def normalise(func):
    vec = func.vector()
    vec /= vec.norm('l2')
    return Function(func.function_space(), vec)
