"""Give a name and make comments"""

def master():

    nbC,nbP,nbTry = gameParameters()

    cache = initCache(nbC,nbP)

    notFound = True

    tries = 1

    print()

    while notFound and (tries<=nbTry):

        print('try',tries)

        well,bad = evaluation(chose(nbC,nbP),cache)

        display(well,bad)

        if well == nbP:

            notFound = False

        else:

            tries += 1

    if tries == nbTry+1:

        print("lost, we had to find:",end=' ')

        displayCache(cache)

    else:

        print("Congratulations, you have found well:", end=' ')

        displyCache(cache)

 

