BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m' '\033[30m'
from tabulate import tabulate

factorservi = 0
def init():
    print(RED)
    while True:
        try:
            factorservi = float(input("Ingresar factor de servico entre 1 y 3: "))
            print("Validacion de numero correcta")
            break
        except ValueError:
            print("El factor de servicio debe ser un numero")
            init()
            
    if(factorservi >= 1 and factorservi <= 3):
                cal(factorservi)   
    else:
        print("El factor de servicio no es correcto")
        init()
    print(RESET)

def cal(parametro):
    print(GREEN)
    while True:
        try:
            caudal = float(input("Ingresar caudal: "))
            break
        except ValueError:
            print("El caudal debe ser un numero")
            cal(parametro)
    while True:
        try:
            tentrada = float(input("Ingresar Temp entrada: "))
            break
        except ValueError:
            print("El Temp de entrada debe ser un numero")
            cal(parametro)
             
    while True:
        try:
            tsalida = float(input("Ingresar Temp salida: "))
            break
        except ValueError:
            print("El Temp de salida debe ser un numero")
            cal(parametro)
    print(RESET)

    consta1 = 1000
    consta2 = 0.0003069

    tamanioDT = round(caudal*(tentrada - tsalida)*parametro*consta1*consta2)

    print("\n El distrito mide ", tamanioDT , '\n')
    chillers(tamanioDT)

def chillers(tdt):
    print(MAGENTA)
    print("\nTamaños de chillers Centrífuos y de Absorción 500TR, 750TR, 1000TR \n")
    print("Favor indicar cantidad y lea con detenimiento \n")
    print("__________________________________________________________ \n")
   
    print(CYAN)
    while True:
        try:
            c500 = int(input("Ingrese cantidad para 500TR centrífugos: "))
        except ValueError:
            print("La cantidad de centrifugado debe ser un numero")
            chillers(tdt)
        while True:
            try:
                c750 = int(input("Ingrese cantidad para 750TR centrífugos: "))
            except ValueError:
                print("La cantidad de centrifugado debe ser un numero")
                chillers(tdt)

            while True:
                try:
                    c1000 = int(input("Ingrese cantidad para 1000TR centrífugos: "))
                except ValueError:
                    print("La cantidad de centrifugado debe ser un numero")
                    chillers(tdt)
                break

            while True:
                try:
                    aa500 = int(input("Ingrese cantidad para 500TR Absorción: "))
                except ValueError:
                    print("La cantidad para la absorcion debe ser un numero")
                    chillers(tdt)
                break

            while True:
                try:
                    a750 = int(input("Ingrese cantidad para 750TR Absorción: "))
                except ValueError:
                    print("La cantidad para la absorcion debe ser un numero")
                    chillers(tdt)
                    break
                while True:
                    try:
                        a1000 = int(input("Ingrese cantidad para 1000TR Absorción: "))
                    except ValueError:
                        print("La cantidad para la absorcion debe ser un numero")
                        chillers(tdt)
                    break
                print(RESET)

                #Operación centrífugos
                totalc=int (500*c500)+(750*c750)+(1000*c1000)
                totala=int (500*aa500)+(750*a750)+(1000*a1000)
                totales = totala + totalc
                tmax = tdt + (tdt*0.5) #Se comprueba el tamaño maximo de TR

                print(BLUE)
                if totales<=tdt:
                            print("\n Las tecnologías seleccionadas no suministran el tamaño del DT \n")
                            print("__________________________________________________________ \n")
                            chillers(tdt)
                elif totales >= tmax:
                            print("\n Las tecnologías seleccionadas superan el tope del DT")
                            print("__________________________________________________________ \n")
                            chillers(tdt)
                else:
                            centrifugos(totalc)
                            absorcion(totala)
                            print(RESET)

def centrifugos(parametro1):
    
    rp=int ((parametro1*0.3190995427365))
    g=int ((parametro1*511.13199046407)/1000)
    c=int ((parametro1*0.0035174111853)*(1925000/0.88))
    o=int ((c*0.03))	
    	
    capex=int (parametro1*0.0035174111853)	
    ft=int((capex*1000000))
    e=int ((capex*1700000))	
    b=int ((capex*2000000))
    crearTablas('centri')
    print(RED) #COLOR
    consta2=1000
    # impresion de tabla
    tabla=[
       ["Energia","emisiones co2(TCo2 al mes)","Capex(Dolares  Megavatios)","Opex(Do-año)"],
       ["Red Publica", +rp, +g,+o],
       ["Microturbina a gas",+g, +c,+o],
       ["Solar fotovoltaica", +ft, +e,+b],
       ["Energia eolica", +b,+capex,+o],
       ["energia biomasa",+capex,+ft,+b],
       ["TR de los chillers centrifugos:",consta2]
      ]
    print(tabulate(tabla))
    print(RESET) #quitar color

def absorcion(parametro2):

    g=int ((parametro2*511.13199046407)/1000)	
    c=int ((parametro2 * 0.0035174111853)*(1925000/0.88))		
    o=int ((c*0.03))		
  		
    capex=int (parametro2*0.0035174111853)		
    ft=int ((capex*1000000)*1.015)		
    b=int ((capex*2000000)) 		
    crearTablas('abso')

    consta3=2000
    print(GREEN) # color
    tabla=[
       ["Energia","emisiones co2(TCo2 al mes)","Capex(Dolares  Megavatios)","Opex(Do-año)"],
       ["Microturbina a gas",+g, +c,+o],
       ["Solar termico", +ft, +o,+b],
       ["energia biomasa",+capex,+ft,+b],
       ["TR de los chillers absorcion:",consta3]
      ]
    print(tabulate(tabla))
    print(RESET) # fin color

def crearTablas(resp):
    if resp == 'centri':
        print("\n Tabla Centrífugos")	
    elif resp == 'abso':
        print("\n Tabla Absorción")	


init()