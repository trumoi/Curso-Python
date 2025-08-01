class Numero:
    def __init__(self, numero):
        self.numero = numero
    
    def evaluar_numero(self):
        if self.numero % 2 != 0:
            print("El numero ingresado es impar")
            if self.numero == 7:
                print("\n Y es un comodín")
        else:
            print("El numero ingresado es par")
            if self.numero ==10:
                print("\n Y es el numero 10")
    
    def sumar(self, numero2):
        return self.numero + numero2
    
if __name__ == "__main__":
    print("===Evalua paridad y suma===")
    valor1 = int(input("Ingrese un número: "))
    numero = Numero(valor1)
    numero.evaluar_numero()
    valor2 = int(input("Ingrese otro numero "))
    suma = numero.sumar(valor2)
    print(f"\nLa suma es : {suma}")
    
    
    
    