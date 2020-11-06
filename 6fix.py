def gameParameters(): # défini une fonction 

    nbC = int(input('Input the number of colors: ')) # variable, nous demande le nombre de couleur

    nbP = int(input('Enter the length of the sequence to guess: ')) # variable, nous demande la longueur de la séquence à deviner

    nbTry = int(input('Enter the number of trials: ')) # variable, nous demande le nombre d'essais

    return nbC,nbP,nbTry # retourne les valeurs des trois variables