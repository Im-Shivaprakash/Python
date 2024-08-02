def evenlyDivides (N):
    # code here
    str_N = str(N)
    count = 0
    
    for i in str_N:
        if i != '0' :
            if N % int(i) == 0:
                count += 1

    return count

print(evenlyDivides(22074))