

cantidad = float(input("Cantidad a invertir:"))
interes = float(input("Ingrese el Intere:"))
años= int(input("Ingrese los años:"))



InteresCalculado=cantidad*interes

for i in (1, años):
    InteresTotal=InteresCalculado*i

print("El interes generado Total es de:", InteresTotal)
print("El interes calculado de aceurdo a los años agendado es de:",InteresTotal)
print("El interes de generado de acuedo a la capital es de:", InteresCalculado)