import random
import os
os.system("cls")

resultado = random.randint()
h = int(input("Heitor: "))
e = int(input("Enzo: "))
if h == resultado and e == resultado:
    print("Os dois acertaram")
elif h == resultado and e != resultado:
    print("Heitor acertou")
elif h != resultado and e == resultado:
    print("Enzo acertou")
elif h != resultado and e != resultado:
    print("Burro pra crlh")