def maxprof(arr):
    incl = 0
    excl = 0
    for i in arr :
        new_excl = excl if excl > incl else incl
        incl = excl + i
        excl = new_excl
    return (excl if excl > incl else incl)

arr = [6,5,10,100,6]
result = maxprof(arr)
print(result)