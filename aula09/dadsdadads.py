# FORMA 1
import bibliotecas
print(bibliotecas.isfloat("4.6"))

# FORMA 2
from bibliotecas import *
print(isint("575"))

# FORMA 3
from bibliotecas import isint, isfloat
print(isint("1234"))

# FOMAR 4
import bibliotecas as b
print(b.isfloat("123.45"))