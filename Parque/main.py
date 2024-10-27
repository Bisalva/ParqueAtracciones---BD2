from modulos.clases import *
import random

parque = Parque(nombre="Praderas", juegos=["Paseo Verde","Paseo Azul","Paseo Infantil","Montaña Rusa"])

atraccion_item_A = Atraccion(nombre="PaseoVerde",capacidad=10,duracion=10,estado=Estado.ACTIVO,cola=0)
atraccion_item_B = Atraccion(nombre="PaseoAzul",capacidad=5,duracion=10,estado=Estado.ACTIVO,cola=0)
atraccion_item_INF = Atraccion_Infantil(edad_limite=10,nombre="PaseoInfantil",capacidad=3,duracion=5,estado=Estado.ACTIVO,cola=0)
atraccion_item_MONTAÑA = Montaña_Rusa(velocidad_maxima=10,altura_maxima=140,extension=1000,nombre="MontañaRusa",capacidad=20,duracion=10,estado=Estado.ACTIVO,cola=0)
#Los parametros tienen su nombre correspondiente para un mayor entendimiento al ser muchas variables ; ej : nombre = "paseoInfantil"

visitante_item_a = Visitante(nombre="Benja",edad=25,altura=1.77,dinero=5000,tickets=0)
visitante_item_b = Visitante(nombre="Nico",edad=20,altura=1.80,dinero=7000,tickets=0)
visitante_item_c = Visitante(nombre="Felipe",edad=7,altura=1.30,dinero=3000,tickets=0)
#En mi script se usaran 3 objetos visitante, pero se pueden agregar los que se requieran

dia = 0
opcion = 0

while True :

    dia += 1
    
    print("\n====Parque de Atracciones====\n")
    print("Dia : ",dia)
    print(f"El dia de hoy entran al parque {Visitante.contar_visitante()} visitantes")


    # Configuracion del estado inicial del parque (CAMBIAR A METODO) - Necesario un archivo extra para los metodos y simplificar el script
    print("\nEstado del Parque : \n")
    atraccion_item_A.estadoInfo(random.randint(1,2))
    atraccion_item_B.estadoInfo(random.randint(1,2))
    atraccion_item_INF.estadoInfo(random.randint(1,2))
    atraccion_item_MONTAÑA.estadoInfo(random.randint(1,2))
    # 1 = Paseo Verde
    # 2 = Paseo Azul
    # 3 = Paseo Infantil
    # 4 = Montaña Rusa

    # Metodo que entrega una lista con el estado de cada juego ( Cada dia cambia )
    parque.consultar_juegos_activos(atraccion_item_A.estado,atraccion_item_B.estado,atraccion_item_INF.estado,atraccion_item_MONTAÑA.estado,atraccion_item_A.nombre,atraccion_item_B.nombre,atraccion_item_INF.nombre,atraccion_item_MONTAÑA.nombre)


    for _ in range(Visitante.contar_visitante()):
        compraRandom = random.randint(1,4)
        # 1 = Paseo Verde
        # 2 = Paseo Azul
        # 3 = Paseo Infantil
        # 4 = Montaña Rusa

    
    #opcion = int(input("\nSalir de la Simulacion del Parque :\n 1 - SI \n 2 - NO \n Opcion : "))
    print("\n")
    opcion = 1
    if opcion == 1 :
        break
    







# atraccion_item_INF.verificar_atraccion(visitante_item_a.edad) - Llama a una funcion con parametros a usar 
# atraccion_item_A.iniciar_ronda() - Llama la funcion
# atraccion_item_INF.iniciar_ronda() Llama la funcion desde la Herencia
# print (atraccion_item_INF.info()) - Imprime la informacion de Atraccion (Herencia)
# print (atraccion_item_A.estadoInfo()) - Imprime la informacion de Atraccion
# print (visitante_item_a.info()) - Imprime la informacion de Visitante
