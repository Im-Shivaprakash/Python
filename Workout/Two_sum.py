def hasArrayTwoCandidates(arr, x):
    # code here
    hash_map = {}
    
    for i in range(len(arr)):
        value = x - arr[i]
        if value in hash_map:
            return 'true'
        else:
            hash_map[arr[i]] = i
        
    return 'false'

arr = [335, 501, 170, 725, 479, 359, 963, 465, 706, 146, 282, 828, 962, 492, 996, 943, 828, 437, 392, 605, 903, 154, 293, 383, 422, 717, 719, 896, 448, 727, 772, 539, 870, 913, 668, 300, 36, 895, 704, 812, 323, 334]
x = 468
result = hasArrayTwoCandidates(arr, x)
print(result)