# RIGHT ROTATION

# [1, 2, 3, 4]
# [4, 1, 2, 3] --- 1 ROTATION
# [3, 4, 1, 2] --- 2 ROTATION

def right_rotation(rotation_number:int, array:list) :
    return array[-rotation_number:] + array[:-rotation_number]

print(right_rotation(2, [1, 2, 3, 4, 5, 6]))
