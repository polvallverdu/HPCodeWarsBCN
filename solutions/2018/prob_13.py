
# el ejercicio consistia en hacer una calculadora de equaciones de segundo grado
coeficientes = input()
# separo los coeficientes
a, b, c = coeficientes.split()
# calculo lo que esta dentrode la raiz
calculoraiz = float(b)**2 - 4*float(a)*float(c)
# si lo que esta dentro de la reiz es negativo pongo que no se puede resolver, si es positivo resuelvo las dos equaciones
# tanto la negativa como positiva
if(calculoraiz < 0):
    print('It has complex Roots!')
else:
    equacion_negativa = (-float(b) - calculoraiz**0.5)/2*float(a)
    print('x_+ =', round(equacion_negativa, 2))
    equacion_positviva = (-float(b) + calculoraiz**0.5)/2*float(a)
    print('x_- =', round(equacion_positviva, 2))
