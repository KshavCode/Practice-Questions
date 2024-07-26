a = "My Name is Jessa"
reversedsentence = []

sentencelist = a.split()
for i in sentencelist :
    reversedword = []
    for j in range(len(i)-1, -1, -1) :
        reversedword.append(i[j])
    reversedword = "".join(reversedword)
    reversedsentence.append(reversedword)

reverse = " ".join(reversedsentence)
print(reverse)
