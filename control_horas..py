def calcular_horas_totales(horas):
    return sum(horas)

def clasificar_jornada(total_horas):
    if total_horas > 40:
        return "Sobretiempo"
    else:
        return "Horario Estándar"

def main():
    trabajadores = [
        ["Juan", 8, 9, 8, 10, 7],
        ["Ana", 7, 8, 7, 8, 7],
        ["Luis", 9, 9, 10, 8, 9],
        ["Maria", 6, 7, 6, 7, 6]
    ]
    while True:
        print("\n=== SISTEMA DE CONTROL DE HORAS ===")
        print("1. Ver resumen de horas")
        print("2. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            print("\n--- RESUMEN DE HORAS TRABAJADAS ---\n")

            for trabajador in trabajadores:
                nombre = trabajador[0]
                horas = trabajador[1:]

                total = calcular_horas_totales(horas)
                clasificacion = clasificar_jornada(total)

                print(f"{nombre} → Total horas: {total} → {clasificacion}")

        elif opcion == "2":
            print("\nSaliendo del sistema...")
            break  # 

        else:
            print("\n Opción inválida")


if __name__ == "__main__":
    main()