def remove_dup(string:str) :
    already_list = []
    new_string = []
    for i in list(string) :
        if i not in already_list : 
            already_list.append(i)
            new_string.append(i)
    return "".join(new_string)

string = "ababacccddded"
print(remove_dup(string))