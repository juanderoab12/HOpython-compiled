import ctypes as C
import numpy as np

math = C.CDLL('./libmymath.so')
math.add_float.restype = C.c_float
math.add_float.argtypes = [C.c_float, C.c_float]
val = math.add_float(3, 4)
print(val)

math.add_int.restype = C.c_int 
math.add_int.argtypes = [C.c_int, C.c_int]
val = math.add_int(3, 4)
print(val)

ini = (C.c_float * 1 )  (3 )
ini2 = (C.c_float * 1 )  (4 )
ini3 = (C.c_float * 1 )  ( )
val = math.add_float_ref(C.byref(ini), C.byref(ini2), C.byref(ini3))
print(val)

ini = (C.c_int * 1 )  (3 )
ini2 = (C.c_int * 1 )  (4 )
ini3 = (C.c_int * 1 )  ( )
val=math.add_int_ref(C.byref(ini),C.byref(ini2),C.byref(ini3))
print(val)

in4 = C.c_int(3)
in1 = (C.c_int * 3 )  (1,2,3 ) 
in2 = (C.c_int * 3 )  (5,3,4 )  
in3 = (C.c_int * 3 )  (0,0,0 )   
math.add_int_array(C.byref(in1), C.byref(in2), C.byref(in3) ,in4)  ## Cref solo punteross
print('suma', in3[:])

math.dot_product.restype = C.c_float
math.dot_product.argtypes = [C.c_float * 3, C.c_float * 3, C.c_int]
in3 = C.c_int(3) 
in1 = (C.c_float * 3 )  (7,2,2 )
in2 = (C.c_float * 3 )  (1,1,1 )  
val = math.dot_product( in1 , in2  , in3 )
print('dot2', val) 
