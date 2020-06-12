def permutation(list1,low,high,list2):
    if (low==high):
        temp = "".join(list1)
        if(temp not in list2):
            list2.append(temp)
    else:
        for i in range(low,high+1):
            list1[low],list1[i]=list1[i],list1[low]
            permutation(list1,low+1,high,list2)
            list1[low],list1[i]=list1[i],list1[low]
    return list2

string = "113"
list1 = list(string)
list2 = []
high = len(list1)-1
permutation(list1,0,high,list2)
# list2 = list(dict.fromkeys(list2))
print(list2)