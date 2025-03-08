# O(n)
def anagram_method1(string1:str, string2:str) :
    if len(string1) != len(string2) :
        return False 
    string1_occ = dict()
    string2_occ = dict()
    for i in range(len(string1)) :
        if string1[i].lower() not in string1_occ :
            string1_occ[string1[i].lower()] = 0
        if string2[i].lower() not in string2_occ :
            string2_occ[string2[i].lower()] = 0
        string1_occ[string1[i].lower()] += 1
        string2_occ[string2[i].lower()] += 1
    return string1_occ == string2_occ

# O(n)
# Suitable only for even number for string comparisions, i.e. string1, string2 and string3 comparisons will result in failure of this function
def anagram_method2(string1:str, string2:str) :
    if len(string1) != len(string2) :
        return False 
    string_occurence = dict()
    for i in range(len(string1)) :
        if string1[i].lower() not in string_occurence :
            string_occurence[string1[i].lower()] = 0
        if string2[i].lower() not in string_occurence :
            string_occurence[string2[i].lower()] = 0
        string_occurence[string1[i].lower()] += 1
        string_occurence[string2[i].lower()] += 1
    return (all(x%2==0 for x in string_occurence.values()))

# SHORTEST WAY, O(n log n)
def anagram_method3(string1:str, string2:str) :
    if len(string1) != len(string2) :
        return False 
    list1 = sorted(string1.lower())
    list2 = sorted(string2.lower())
    return list1 == list2

a = "Danger"   
b = "garden"
print(anagram_method1(a, b))
print(anagram_method2(a, b))
print(anagram_method3(a, b))
    
