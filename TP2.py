"""Give a name and make comments"""

def chooseGame(Self,possibles,results,tries):

    if tries == 1:

        return [1,1,2,2]

    elif len(Self)==1 :
        retrn.Self.pop()
        

    else:

        return max(possibles, key=lambda x: min(sum(1 for p in S if evaluation(p,x) != res) for res in results))