string1 = "1a1b1a2g"
arr = []
for i in range(len(string1)):
    if(string1[i].isdigit()==True):
        for j in range(int(string1[i])):
            arr.append(string1[i+1])
print("".join(arr))