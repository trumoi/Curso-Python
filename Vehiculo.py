class vehiculo :
    def __init__ (self, marca, modelo, velocidad) :
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
    def mostrar_info (self) :
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Velocidad: {self.velocidad}")
    
def main():
    # vehículo 1
    print("\nIntroduce los datos del primer vehículo:")
    marca1 = input("Marca: ")
    modelo1 = input("Modelo: ")
    velocidad1 = input("Velocidad: ")
    veh1 = vehiculo(marca1, modelo1, velocidad1)

    # vehículo 2
    print("\nIntroduce los datos del segundo vehículo:")
    marca2 = input("Marca: ")
    modelo2 = input("Modelo: ")
    velocidad2 = input("Velocidad: ")
    veh2 = vehiculo(marca2, modelo2, velocidad2)

    # Bucle de modificación
    while True:
        print("\n¿Deseas modificar la velocidad de algún vehículo? ")
        opcion = input("Escribe '1 para veh1' o '2 para veh2'' o 'N' para salir ").lower()
                    
        if opcion == "1":
            veh1.velocidad = int(input("Introduce la nueva velocidad para veh1 (km/h): "))
           
        elif opcion == "2":
            veh2.velocidad = int(input("Introduce la nueva velocidad para veh2 (km/h): "))       
        else:
            break
    
    # Mostrar información actualizada
    print("\nInformación actualizada:")
    veh1.mostrar_info()
    veh2.mostrar_info() 

if __name__ == "__main__":
    main()