import os

trabajadores = []
cargos_disponibles = ['CEO', 'Desarrollador', 'Analista de datos']
while True:
        print("\n=== SISTEMA DE SUELDOS ===")
        print("1.- Registrar trabajador")
        print("2.- Listar todos los trabajadores")
        print("3.- Imprimir planilla de sueldos")
        print("4.- Salir del Programa")
        print ()

        opcion = input("Ingrese la opción de su preferencia: ")
        
        opcion = int(opcion)
        
        if opcion == 1:
            print("\n=== REGISTRO NUEVO TRABAJADOR ===")
            nombre = input("Ingrese nombre y apellido del trabajador: ")
            cargo = input("Ingrese cargo del trabajador (CEO, Desarrollador, Analista de datos): ")
            sueldo_bruto = input("Ingrese sueldo bruto del trabajador: ")
            
            if nombre and cargo and sueldo_bruto:
                try:
                    sueldo_bruto = float(sueldo_bruto)
                except ValueError:
                    print("El sueldo bruto debe contener numeros.")
                    continue
                
                if cargo == 'CEO':
                    desc_salud = 70000
                    desc_afp = 120000
                elif cargo == 'Desarrollador':
                    desc_salud = 60000
                    desc_afp = 100000
                elif cargo == 'Analista de datos':
                    desc_salud = 50000
                    desc_afp = 90000
                else:
                    print("Cargo incorrecto.")
                    continue

                desc_salud = sueldo_bruto * 0.07 
                desc_afp = sueldo_bruto * 0.12  
                liquido_pagar = sueldo_bruto - desc_salud - desc_afp
                trabajadores.append([nombre, cargo, sueldo_bruto, desc_salud, desc_afp, liquido_pagar])
                
                print("Trabajador registrado correctamente.")
            else:
                print("Debe ingresar todos los datos solicitados.")
        
        elif opcion == 2:
            print("\n=== LISTA DE TODOS LOS TRABAJADORES ===")
            if not trabajadores:
                print("No hay trabajadores registrados.")
            else:
                for trabajador in trabajadores:
                     print(f"Nombre: {trabajador[0]}, Cargo: {trabajador[1]}, Sueldo Bruto: {trabajador[2]}, "
                          f"Descuento Salud: {trabajador[3]}, Descuento AFP: {trabajador[4]}, Sueldo líquido a pagar: {trabajador[5]}")
        elif opcion == 3:
            print("\n=== IMPRIMIR PLANILLA DE SUELDOS ===")
            if not trabajadores:
                print("No hay trabajadores registrados para imprimir la planilla.")
            else:
                print("Cargos disponibles para imprimir:")
                for index, cargo in enumerate(cargos_disponibles, start=1):
                    print(f"{index}. {cargo}")
                
                opcion_cargo = input("Ingrese el número del cargo para imprimir su planilla (o 'todos' para imprimir todos): ")
                
                if opcion_cargo.lower() == 'todos':
                    # Imprimir todos los trabajadores en un archivo txt
                    with open('sueldos_trabajadores.txt', 'w', newline='') as archivo:
                        archivo.write("Nombre Cargo Sueldo Bruto Descuento Salud Descuento AFP Sueldo Liquido a pagar")
                    print("Se ha generado el archivo 'sueldos_trabajadores.txt' correctamente.")
                
                elif opcion_cargo.isdigit() and int(opcion_cargo) <= len(cargos_disponibles):
                    cargo_seleccionado = cargos_disponibles[int(opcion_cargo) - 1]
                    filename = f'planilla_{cargo_seleccionado.lower().replace(" ", "_")}.txt'
                    
                    with open(filename, 'w', newline='') as archivo:
                        archivo.write("Nombre Cargo Sueldo Bruto Descuento Salud Descuento AFP Sueldo Liquido a pagar'")                    
                    print(f"Se ha generado el archivo '{filename.txt}' correctamente.")
                else:
                    print("Opción no válida.")
        
        elif opcion == 4:
            print("¡Hasta Luego!")
            break
        

