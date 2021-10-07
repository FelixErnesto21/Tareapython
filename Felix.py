from datetime import datetime 
import os 


#reinvertimos la fecha
def inv_fecha(fec):
    fen = datetime.strptime(fec,'%d/%m/%Y')
    return datetime.strftime(fen,'%Y-%m-%d')

#se hace el calculo del Bono1 y Bono2
def pago(sueldobase,horas,valor1,valor2):
    
    if int(horas) <= 5:
        calculo= float(sueldobase) + float(sueldobase) / 0.05 * float(valor1)
    else:
        calculo= float(sueldobase) + float(sueldobase) / 1.5 * float(valor2)
    return float(calculo)

#datos a solicitar para calcular los bonos segun horas extras semanales
bono_general = float(input('Intoduzca bono General:'))
bono_eficiencia = float(input('Intoduzca bono Eficiencia:'))


f = open("pago_nomina_12sep2021.txt", "w")

#Leeo el archivo txt
with open("Archivo nomina.txt", "r") as pagos:
    for linea in pagos:

        campo = linea.split()

        
        if campo[0].isdigit():
            fec = inv_fecha(campo[1])
            suel = pago(campo[4].replace("$",""),campo[5],bono_general,bono_eficiencia)
        else:
            fec = campo[1]
            suel = campo[3]

        
      
        f.write(campo[0]+" ")
        f.write(fec+" ")
        f.write(campo[2]+" ")
        f.write(campo[3]+" ")
        f.write(campo[4]+" ")
        

       
        if campo[0].isdigit():
            f.write(campo[5]+" ")
            f.write(str(suel))
            f.write(os.linesep)
        else:
            f.write(os.linesep)
           
        

f.close()

