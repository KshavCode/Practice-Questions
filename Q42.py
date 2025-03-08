def swap(string:str, location1:int, location2:int) :
    if location1<0 or location1>len(string) or location2<0 or location2>len(string) :
        return "ERROR"
    string_list = list(string)
    temp = string_list[location1]
    string_list[location1] = string_list[location2]
    string_list[location2] = temp
    return "".join(string_list)

def backtrack(string:str, id=0, permutation=[]) :
    if len(string)-1==id :
        permutation.append(string)
        return
    for i in range(id, len(string)) :
        string = swap(string, i, id)
        backtrack(string, id+1, permutation)
    return permutation
    
print(backtrack("ABCD"))