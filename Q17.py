def matchstring(originalarray:list, queryarray:list) -> list :
    resultarray = [0 for i in queryarray]
    for i in range(len(queryarray)) :
        for j in range(len(originalarray)) :
            if queryarray[i] == originalarray[j] :
                resultarray[i] += 1

    return resultarray



print(matchstring(["ab", "abc", "cd", "cd"], ["cd", "abc", "a"]))