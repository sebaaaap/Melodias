def transponer():
    
    notas = ["do", "do#", "re", "re#", "mi", "fa", "fa#", "sol", "sol#", "la", "la#", "si"]
     

    melodia = input("Ingrese la melodía: ")
    melodia = melodia.strip()
    lista_melodias = melodia.split()

    print('soy la lista con las melodias:', lista_melodias)
    
    inter = input("Ingrese el intervalo: ")
    inter = inter.strip()
    

    def definir_semitono(inter): 
        semitono = 0

        if inter == "1":
            semitono = 0
            return semitono

        elif inter == "2":
            semitono = 2
            return semitono
        
        elif inter == "3":
            semitono = 4
            return semitono
        
        elif inter == "4":
            semitono = 5
            return semitono
        
        elif inter == "T":
            semitono = 6
            return semitono
        
        elif inter == "5":
            semitono = 7
            return semitono
        elif inter == "6":
            semitono = 9
            return semitono
        
        elif inter == "7":
            semitono = 11
            return semitono
        
        elif inter == "8":
            semitono = 12
            return semitono
        
        elif inter == "2m":
            semitono = 1
            return semitono
        
        elif inter == "3m":
            semitono = 3
            return semitono
        
        elif inter == "6m":
            semitono = 8
            return semitono
        
        elif inter == "7m":
            semitono = 10
            return semitono
        
    def buscar_indice(lista, nota): 
        for indice in lista : 
            if lista[indice] == nota: 
                return indice
    
    def sumarsemitono(lista, melodias): 
        print('aqui va la logia de la transpuesta')

    def listafinal(lista):
        print('hola')

    transformadas = []

    for nota in melodia:
        i = 0
        while i < len(nota) and not nota[i].isdigit():
            i += 1
        notaCentral = nota[:i]
        octava = int(nota[i:])

        posicion = -1
        for i in range(len(notas)):
            if notas[i] == notaCentral:
                posicion = i
        
        nuevaPos = (posicion + semitono) % 12
        nuevaOctava = octava + (posicion + semitono) // 12

        transformada = notas[nuevaPos] + str(nuevaOctava)

        transformadas.append(transformada)

    print(" ".join(transformadas))

        

transponer()