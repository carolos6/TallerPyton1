

cantidad = float(input("Cantidad a invertir:"))
interes = float(input("Ingrese el Intere:"))
años= int(input("Ingrese los años:"))



InteresCalculado=cantidad*interes

for i in (1, años+1):
    InteresTotal=InteresCalculado*i

print("El interes generado Total es de:", InteresTotal)