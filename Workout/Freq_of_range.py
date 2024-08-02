
def frequencyCount(arr, N, P):
    # code here
    count = [0 for i in range(N)]
    
    for i in arr:
        if i < len(count)+1:
            count[i-1] += 1
    
    return count

arr = [2, 3, 2, 3, 5]
N = 5
P = 5
print(frequencyCount(arr, N, P))

