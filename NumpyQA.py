import numpy as np
# Funciones de numpy

a = np.array([1,2,3,4])
# Saber el tipo de dato
a.dtype
# Crea con el iterador una matriz para este caso y puede especificarse el tipo de dato
np.array([(1.5,2,3),(4,5,6)], dtype=complex)
# Crea una matriz de zeros con la dimensiones determinadas
np.zeros((3,2,3))
# Crea una matriz literalmente vacia de las dimensiones dadas
np.empty((2,3))
# Crea una matriz de unos con la dimensiones determinadas
np.ones((3,2,3))
# Crea una arreglo con valor inicial 10, valor final 100 y paso a paso 7
d = np.arange(10,100,7)
# Si solo le damos un elemento, va de 0 a n-1 
np.arange(9)
# Crea un arreglo con valor inicial 0, final 2 y con 9 elementos
np.linspace(0,2,9)

# La funcion reshape redefine la forma de una arreglo o matriz a la forma deseada 
np.arange(12).reshape(3,4)
np.arange(12).reshape(3,2,2)
# como nota podemos usar -1 como comidin para que el programa establezca el valor deseado y asi adaptar todos los elementos
# con reshape podemos darle diferentes formas y obtener diversas formas ya se de una 2x1 o 1x2

# Operaciones built in
a = np.array([1,2,3,4]).reshape(1,-1) #row vector
b = np.array([1,2,3,4]).reshape(-1,1) #column vector
#Comparaciones
c=(a==b) # 
d=(a*b)
e=(a+b)
f = (a>b)

# Concepto super importante de python 
# Broadcasting: propagar las dimensiones en todas las dimensiones. Adaptar arregllos de diferentes dimensiones