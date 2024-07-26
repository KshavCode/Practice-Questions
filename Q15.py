# LEFT ROTATION
# [4, 5, 6, 8]
# [5, 6, 8, 4]      -- 1 ROTATION
# [6, 8, 4, 5]      -- 2 ROTATION


# MY CODE
def left_rotation(array:list, rotation_number:int=1) -> list:
    newlis = [0 for x in range(len(array))]
    for i in range(len(array)) :
        place = i
        for j in range(rotation_number) :
            if place == 0 :
                place = len(array)
            place -= 1
        newlis[place] = array[i]
    return newlis
        

# BETTER CODE
def left_rotation(array:list, rotation_number:int=1) -> list:
    return array[rotation_number:] + array[:rotation_number]


array = []
length = int(input())
for i in range(length) :
    array.append(int(input()))

print(left_rotation(array, 2))
