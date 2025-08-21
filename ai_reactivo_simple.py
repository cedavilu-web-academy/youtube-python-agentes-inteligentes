# Robot debe ir por un pasillo, teniendo en cuenta que hay obstáculos
def percibir(pasillo,posicion_actual):
    # Simular sensores: Si hay obstáculo debe deternerse y si no debe avanzar
    if posicion_actual +1 < len(pasillo):
       return pasillo[posicion_actual +1 ] == 'obstáculo'
    else:
        return False

def decidir(percepcion_obstaculo):
     # El agente una decisión basada en su percepción actual
     if percepcion_obstaculo == True:
         print("Obstáculo detectado. El agente decide detenerse") 
         return 'detener'
     else:
         print("Camino libre. El agente decide avanzar")
         return 'avanzar'
     
def actuar(accion, posicion_actual):
    # El agente ejecuta la acción dedicida y actualiza su posición  
    if accion == 'avanzar':
        return posicion_actual + 1
    else:
        return posicion_actual
    
def controlador_agente():
    # Simulaer el cilco de vida del agente
    pasillo = ['pasilo libre'] * 10
    pasillo[2] = 'obstáculo'
    pasillo[5] = 'obstáculo'
    pasillo[8] = 'obstáculo'
    posicion_actual = 0
    largo_pasillo = len(pasillo)
    print('--- Agente reactivo en acción ---')
    while posicion_actual < largo_pasillo -1:
        # 1.- Percibir el entorno
        hay_obstaculo = percibir(pasillo,posicion_actual)
        # 2.- Decidir que hacer
        accion = decidir(hay_obstaculo)
        # 3.- Actur según la decisión
        posicion_actual = actuar(accion, posicion_actual)
        print(f"Posición actual: {posicion_actual} \n")

print("--- El agente llegó hasta el final del pasillo--- ")

# Ejecutar el simulador del agente 
controlador_agente()