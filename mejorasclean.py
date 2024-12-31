def transponer():
    # Escala cromática en sostenidos
    notas = ["do", "do#", "re", "re#", "mi", "fa", "fa#", "sol", "sol#", "la", "la#", "si"]

    # Entrada de la melodía y el intervalo
    melodia = input("Ingrese la melodía: ").strip()
    lista_melodias = melodia.split()

    inter = input("Ingrese el intervalo: ").strip()

    # Función para definir cuántos semitonos corresponde al intervalo (usando if-elif)
    def definir_semitono(inter): 
        semitono = 0

        if inter == "1":
            semitono = 0
        elif inter == "2":
            semitono = 2
        elif inter == "3":
            semitono = 4
        elif inter == "4":
            semitono = 5
        elif inter == "T":
            semitono = 6
        elif inter == "5":
            semitono = 7
        elif inter == "6":
            semitono = 9
        elif inter == "7":
            semitono = 11
        elif inter == "8":
            semitono = 12
        elif inter == "2m":
            semitono = 1
        elif inter == "3m":
            semitono = 3
        elif inter == "6m":
            semitono = 8
        elif inter == "7m":
            semitono = 10

        return semitono

    # Función para transponer una nota
    def transponer_nota(nota, semitono):
        # Separar la nota en parte musical y octava
        i = 0
        while i < len(nota) and nota[i] not in "0123456789":
            i += 1

        if i < len(nota):  # Si encontramos un número
            notaCentral = nota[:i]
            octava = int(nota[i:])
        else:  # Si no hay número, asignamos octava por defecto
            notaCentral = nota
            octava = 4

        # Encontrar la posición de la nota en la escala cromática
        posicion = notas.index(notaCentral)

        # Calcular nueva posición y nueva octava
        nuevaPos = (posicion + semitono) % 12
        nuevaOctava = octava + (posicion + semitono) // 12

        # Combinar nota transpuesta con la nueva octava
        return notas[nuevaPos] + str(nuevaOctava)

    # Determinar cuántos semitonos sumar
    semitono = definir_semitono(inter)

    # Transponer todas las notas de la melodía
    transformadas = []
    for nota in lista_melodias:
        transformadas.append(transponer_nota(nota, semitono))

    # Mostrar el resultado nota por nota
    print("Melodía transpuesta:")
    for nota in transformadas:
        print(nota, end=" ")  # Mostramos las notas separadas por espacio
    print()  # Línea final para salto

# Llamar a la función principal
transponer()
