
matricula = int(input("Ingresa tu matricula: "))
carrera = float(input("Ingresa tu carrera (Industrial 1, Telematica 2, Computacion 3, Mecanica 4): "))
semestre = float(input("Ingresa el semestre que cursas: "))
promedio = float(input("Ingresa tu promedio (0-10): "))

if carrera == 1 and semestre >= 6 and promedio >= 8.5:
    print('Matricula: ',matricula,' Carrera: Industrial Promedio: ',promedio)

elif carrera == 2 and semestre >= 5 and promedio >= 9:
    print('Matricula: ',matricula,' Carrera: Telematica Promedio: ',promedio)

elif carrera == 3 and semestre >= 6 and promedio >= 8.8:
    print('Matricula: ',matricula,' Carrera: Industrial Promedio: ',promedio)

elif carrera == 4 and semestre >= 7 and promedio >= 9:
    print('Matricula: ',matricula,' Carrera: Industrial Promedio: ',promedio)
else :
    print('Lo sentimos, no puedes ser asistente de alguna de las carreras que se ofrecen en la universidad')
    