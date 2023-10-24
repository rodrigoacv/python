# 2. Escribe el código de un algoritmo que solicita las notas de dos pruebas, calcula el promedio y luego
#despliega 3 mensajes distintos dependiendo del promedio: “Felicitaciones, vas camino a aprobar”
#(si el promedio es mayor o igual a 4.0); “Atención, vas camino a reprobar” (promedio mayor o igual
#a 3.0 pero menor a 4.0) y “Pocas posibilidades de aprobar” (para promedio menor a 3.0).

prueba1 = float(input('Ingresa nota prueba1:'))
prueba2 = float(input('Ingresa nota prueba1:'))

promedio = (prueba1 + prueba2)/2

if promedio >= 4:
    print('Felicitaciones, vas camino a aprobar')
else:
    if promedio >= 3 and promedio < 4:
        print('Atención, vas camino a reprobar')
    else:
        if promedio < 3:
            print('Pocas posibilidades de aprobar')
        else:
            print('FIN')


