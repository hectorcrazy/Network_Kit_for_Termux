import os
import pyfiglet
import time
#Colores
green="\033[1;32m"
blanco="\033[0m"
amarillo="\033[1;33m"
#Base 1
os.system('clear')
#Banner
pws = pyfiglet.figlet_format("Network Kit")
print(pws)
#Base 2
print(f"{green}Seleccione la Herramienta:\n1.Informacion del Dominio\n2.ping a Host\n3.Configuracion DNS\n4.DNS inverso\n5.Descargar Archivos\n6.Continuar Descarga Parada")
yk = float(input("===> "))
if yk ==1:
    a = input("===> ")
    os.system('whois ' + a)
elif yk ==2:
        b = input("===> ")
        os.system('ping ' + b)
elif yk ==3:
            c = input("===> ")
            os.system('dig ' + c)
elif yk ==4:
                d = input("===> ")
                os.system('dig -x ' + d)
elif yk ==5:
                    e = input("===> ")
                    os.system('wget ' + e)
elif yk ==6:
                        f = input("===> ")
                        os.system('wget -c ' + f)
else:
    print("Error Al Seleccionar La Opcion\nReinicie el Programa")                       
