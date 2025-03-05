def merge_sort(arr):
    if len(arr) == 1:
        return arr
    m = len(arr) // 2
    L = arr[:m]
    R = arr[m:]
    L_arr = merge_sort(L)
    R_arr = merge_sort(R)
    
    l,r = 0,0
    sorted_arr = [0] * len(arr)
    i = 0
    
    while l < len(L_arr) and r < len(R_arr):
        if L_arr[l] < R_arr[r]:
            sorted_arr[i] = L_arr[l]
            l+=1
        else:
            sorted_arr[i] = R_arr[r]
            r+=1
        i+=1
    while l < len(L_arr):
        sorted_arr[i] = L_arr[l]
        l+=1
        i+=1
    while r < len(R_arr):
        sorted_arr[i] = R_arr[r]
        r+=1
        i+=1
        
    return sorted_arr

x=merge_sort([9,3,4,5,7,1,0])
print(x)