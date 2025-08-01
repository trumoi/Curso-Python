
def evaluar_numero():
    numero = int(input("Introduzca un numero "))

    if numero > 10:
        print("❌Numero invalido. Debe estar entre 0 y 10.")
        numero = int(input("Reintroduzca numero "))
    else:
         return numero   
     
def evaluar_paridad(numero):
    if (numero % 2) == 0:
        numero_par(numero)
    else:
        numero_impar(numero)

def numero_par(numero):
    if numero ==10:
        print("El numero ingresado es 10 y Par")
    else:
        print("El numero ingresado es Par")


def numero_impar(numero):
    if numero ==7:
        print("Se ha ingresado un comodin. El numero es impar")
    else:
        print("El numero ingresado es impar")
        
def main():
    numero = evaluar_numero()
    evaluar_paridad(numero)
    
if __name__ == "__main__":
    main()
    
    
    

        
        