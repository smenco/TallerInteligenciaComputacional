
sueldo = float(input("Ingrese el sueldo base"))

ventas = int(input("Ingrese la cantidad de ventas"))

comision = 0.15
final = sueldo + (ventas + comision*100)
print("Salario final del trabajador",final)