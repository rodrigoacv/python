# 3. Escribe el código de un algoritmo que solicite por pantalla el número entero A, y luego el número
# entero B. Luego, debe verificar si A/B produce una división entera (es decir, el resto de la división
# es 0). Si este es el caso, deberá mostrar por pantalla “B divide exactamente a A”. En caso
# contrario “B no divide a A en forma”.

a = int(input('Ingresa número entero: '))
b = int(input('Ingresa número entero: '))
modulo = a%b

#print(modulo)

if modulo == 0:
    print('B divide exactamente a A')
else:
    print('B no divide a A en forma')