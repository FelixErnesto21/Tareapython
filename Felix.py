from datetime import datetime 
import os 


#reinvertimos la fecha
def inv_fecha(fec):
    fen = datetime.strptime(fec,'%d/%m/%Y')
    return datetime.strftime(fen,'%Y-%m-%d')

#se hace el calculo del Bono1 y Bono2
def pago(sueldobase,horas,bono1,bono2):
    
    if int(horas) <= 5:
        calculo= float(sueldobase) + float(sueldobase) / 0.05 * float(bono1)
    else:
        calculo= float(sueldobase) + float(sueldobase) / 1.5 * float(bono2)
    return float(calculo)

#datos a solicitar para calcular los bonos segun horas extras semanales
bono_general = float(input('Intoduzca bono General:'))
bono_eficiencia = float(input('Intoduzca bono Eficiencia:'))


f = open("pago_nomina_12sep2021.txt", "w") # creando el archivo de salida con el sueldo a pagar en una archivo .txt

#Leeo el archivo txt
with open("Archivo nomina.txt", "r") as nomina:
    for linea in nomina:

        datos = linea.split()

        
        if datos[0].isdigit(): # Si el dato en la posicion es Verdadero
            fec = inv_fecha(datos[1]) # Mando a llamar la funcion de inversion de fecha
            suel = pago(datos[4].replace("$",""),datos[5],bono_general,bono_eficiencia)
        else:
            fec = datos[1]
            suel = datos[3]

        
      
        f.write(datos[0]+" ")
        f.write(fec+" ")
        f.write(datos[2]+" ")
        f.write(datos[3]+" ")
        f.write(datos[4]+" ")
        

       
        if datos[0].isdigit():
            f.write(datos[5]+" ")
            f.write(str(suel))
            f.write(os.linesep)
        else:
            f.write(os.linesep)
           
        

f.close() # Cerrando el archivo creado

