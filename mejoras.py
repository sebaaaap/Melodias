def transponer():
    # escala cromática en sosstenidos
    notas = ["do", "do#", "re", "re#", "mi", "fa", "fa#", "sol", "sol#", "la", "la#", "si"]


    melodia = input("Ingrese la melodía: ").strip()
    lista_melodias = melodia.split()

    inter = input("Ingrese el intervalo: ").strip()

    # define cuaantos semitonos hay que sumar
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

    # pasa los bemoles a sostenidos
    def convertir_bemol_a_sostenido(nota):
        # busca los bemoles y devuelve su equivalencia
        if "b" in nota:
            if nota[:3] == "sib":
                return "la#" + nota[3:]  
            elif nota[:3] == "mib":
                return "re#" + nota[3:]
            elif nota[:3] == "lab":
                return "sol#" + nota[3:]
            elif nota[:3] == "reb":
                return "do#" + nota[3:]
            elif nota[:4] == "solb":
                return "fa#" + nota[4:]
            elif nota[:3] == "dob":
                return "si" + nota[3:]
        return nota  # caso contrario retorna la nota normal

    # transpone la nota
    def transponer_nota(nota, semitono):
        # divide la nota en parte musical y octava
        i = 0
        while i < len(nota) and not nota[i].isdigit():
            i += 1

        # si la nota no tiene octva se le asigna 4 
        if i == len(nota):
            notaCentral = nota
            octava = 4  # octava por defecto
        else:
            notaCentral = nota[:i]
            octava = int(nota[i:])

        # pasa los bemoles a sostenidos
        notaCentral = convertir_bemol_a_sostenido(notaCentral)

        # busca la posicion en la escala cromática
        if notaCentral in notas:
            posicion = notas.index(notaCentral)
        else:
            return  # si hay error retorna nada

        
        nuevaPos = (posicion + semitono) % 12 # caclula la nueva posicion
        nuevaOctava = octava + (posicion + semitono) // 12 # calcula la nueva octava

        # entrega la nueva nota y su octava correspondiente
        return notas[nuevaPos] + str(nuevaOctava)

    
    semitono = definir_semitono(inter)

    # aqui traspone cada nota y la transforma
    transformadas = [transponer_nota(nota, semitono) for nota in lista_melodias]

    
    print("Melodía transpuesta:", " ".join(transformadas))


transponer()
