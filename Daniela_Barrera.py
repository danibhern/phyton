import random, csv, statistics, os


trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez",
                "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

def limpiar_pantalla():
    if os.name == 'nt':  
        os.system('cls')
    else:         
        os.system('clear')

def numeros(a):
    return "{:,}".format(a).replace(",", ".")

def generar_sueldos():
    sueldos = [random.randint(300000, 2500000) for i in range(len(trabajadores))]
    return sueldos

def clasificar_sueldos(sueldos):
    clasificacion = {
        "Sueldos menores a $800.000": [],
        "Sueldos entre $800.000 y $2.000.000": [],        
        "Sueldos superiores a $2.000.000": []
    }
    
    for i in sueldos:
        if i < 800000:
            clasificacion["Sueldos menores a $800.000"].append(i)
        elif 800000 <= i <= 2000000:
            clasificacion["Sueldos entre $800.000 y $2.000.000"].append(i)        
        else:
            clasificacion["Sueldos superiores a $2.000.000"].append(i)
    return clasificacion

def generar_reporte(sueldos):
    global reporte
    reporte = []
    for i in range(len(trabajadores)):
        sueldo_base = sueldos[i]
        descuento_salud = int(sueldo_base * 0.07)
        descuento_afp = int(sueldo_base * 0.12)
        sueldo_liquido = sueldo_base - descuento_salud - descuento_afp
        reporte.append([trabajadores[i], numeros(sueldo_base), numeros(descuento_salud), numeros(descuento_afp), numeros(sueldo_liquido)])
    return reporte

def reporte_sueldos():
    print("Nombre empleado\t\tSueldo Base\tDescuento Salud\t    Descuento AFP     Sueldo Líquido")
    for i in reporte:        
        print(f"{i[0]:<24}${i[1]:>10}     ${i[2]:>10}         ${i[3]:>10}       ${i[4]:>10}")
        
def guardar_reporte_csv(reporte):
    with open('reporte_sueldos.csv', mode='w', newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])
        writer.writerows(reporte)


def calcular_estadisticas(sueldos):
    estadisticas = {
        'Sueldo más alto\t\t': max(sueldos),
        'Sueldo más bajo\t\t': min(sueldos),  
        'Promedio de sueldos\t': int(statistics.mean(sueldos)),
        'Media_geometrica\t': (1/10)              
    }    
    return estadisticas

def menu():
    sueldos = []
    while True:
        limpiar_pantalla()        
        print("Menú de opciones: ".center(29, "="))
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadisticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")
        try:    
            opcion = input("\nSeleccione una opción: -> ")

            if opcion == "1":
                limpiar_pantalla()
                if not sueldos:
                    sueldos = generar_sueldos()
                    print("Sueldos generados correctamente")
                    input("\nPresione Enter para continuar...")
                else:
                    limpiar_pantalla()
                    print("Los sueldos ya fueron generados")
                    while True:
                        reemplazar = input("¿Desea reemplazar los sueldos? (s/n): ").lower().strip()
                        if reemplazar == "s":
                            sueldos = generar_sueldos()
                            limpiar_pantalla()
                            print("Sueldos reemplazados correctamente")
                            input("\nPresione Enter para continuar...")
                            break
                        elif reemplazar == "n":
                            break
                        else:
                            limpiar_pantalla()
                            print("Opción no válida")
                            input("\nPresione Enter para continuar...")
                            
            elif opcion == "2":
                if not sueldos:
                    limpiar_pantalla()
                    print("Debe asignar sueldos primero")
                    input("\nPresione Enter para continuar...")                
                else:
                    clasificacion = clasificar_sueldos(sueldos)
                    limpiar_pantalla()
                    for rango, lista in clasificacion.items():
                        
                        print(f"{rango:29s}   TOTAL:{len(lista)}")
                        if lista:
                            print("\nNombre empleado\t\t\tSueldo")
                        for sueldo in lista:
                            empleado_index = sueldos.index(sueldo)
                            empleado = trabajadores[empleado_index]
                            print(f"{empleado:30s}\t${numeros(sueldo):>10s}")
                        print("")
                    acumulado = sum(sueldos)
                    print(f"TOTAL SUELDOS:\t\t\t${numeros(acumulado):>10s}")
                    input("\nPresione Enter para continuar...")
                    
            elif opcion == "3":
                if not sueldos:
                    limpiar_pantalla()
                    print("Debe asignar sueldos primero")
                    input("\nPresione Enter para continuar...")   
                else:
                    estadisticas = calcular_estadisticas(sueldos)
                    limpiar_pantalla()
                    print("Estadísticas de sueldos:")
                    for parametro, valor in estadisticas.items():
                        print(f"{parametro}:\t${numeros(valor)}")
                    input("\nPresione Enter para continuar...")                

            elif opcion == "4":
                if not sueldos:
                    limpiar_pantalla()
                    print("Debe asignar sueldos primero")
                    input("\nPresione Enter para continuar...")   
                else:
                    reporte = generar_reporte(sueldos)
                    guardar_reporte_csv(reporte)                
                    limpiar_pantalla()                
                    print("Reporte generado correctamente a archivo CSV\n")
                    reporte_sueldos()
                    input("\nPresione Enter para continuar...")
                    
            elif opcion == "5":
                limpiar_pantalla()
                print("Finalizando programa...")
                print("Desarrollado por Daniela Barrera")
                print("RUT 17.682.429-8")
                break
            else:
                print("Opción no válida")
        except:
            print("Operación no válida")
menu()