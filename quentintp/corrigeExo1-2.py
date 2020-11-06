from random import randint

"""Give a name and make comments"""

def initCache(nbColors=6,nbPawns=4):

    return [randint(1,nbColors) for i in range(nbPawns)]

 

"""Give a name and make comments"""

def choose(nbColors=6,nbPawns=4):

    nocorrect = True

    while nocorrect:

        nocorrect = False

        selected = input('Input your proposal: ')

        if len(selected) == nbPawns:

            selected = [int(x) for x in list(selected)]

            for x in selected:

                if (x<1) or (x>nbColors):

                    nocorrect = True

        else:

            nocorrect = True

    return selected
