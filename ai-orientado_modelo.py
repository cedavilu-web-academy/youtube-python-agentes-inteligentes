def percibir_y_modelar(pasillo_real):
    modelo = {}
    for i,estado in enumerate(pasillo_real):
        modelo[i] = estado

    return modelo    

def decidir_ruta(modelo_interno):
    # El agente usa el modelo para planificar la ruta completa antes de empezar
    print('--- El agente planifica la ruta más eficiente---')
    ruta_planificada = []
    posicion_actual = 0
    largo_pasillo = len(modelo_interno)
    while posicion_actual < largo_pasillo:
        # El agente consulta su modelo interno para cada paso
        ruta_planificada.append(posicion_actual)
        if modelo_interno.get(posicion_actual + 1) == 'obstáculo':
            # Lo que debería hacer el agente es saltar ese obstáculo
            print(f"Planificando: Salta el obstáculo en la posición {posicion_actual +1}")
            posicion_actual += 2
            # posicion_actual = posicion_actual +2
        else:
            # Si está libre el camino, la idea es avanzar
            posicion_actual += 1 

    return ruta_planificada

def actuar_en_ruta(ruta):
    # El agente debe recorrer cada paso de la ruta planificado
    print('--- El egente ejecuta su plan ---')
    for paso in ruta:
        print(f"Movimiento: El agente avanza a la posición: {paso}")

def contrador_modelo():
    # Simular el ciclo del agente
    pasillo_real = ['pasillo libre'] * 10
    pasillo_real[2] = 'obstáculo'
    pasillo_real[5] = 'obstáculo'
    pasillo_real[8] = 'obstáculo'

    # 1.- Percibir y crear el modelo interno
    modelo = percibir_y_modelar(pasillo_real)
    # 2.- Decidir planifica la ruta
    ruta_a_seguir = decidir_ruta(modelo)
    # 3.- Actuar y debe ejecutar la ruta planificada
    actuar_en_ruta(ruta_a_seguir)

print("\n --- El agente orientado a modelo, llegó al final del pasillo---")

# Ejecutar el llamado a la función
contrador_modelo()


        