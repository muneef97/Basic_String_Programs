def permutation(list1,low,high):
    if (low==high):
        print ("".join(list1))
    else:
        for i in range(low,high+1):
            list1[low],list1[i]=list1[i],list1[low]
            permutation(list1,low+1,high)
            list1[low],list1[i]=list1[i],list1[low]


string = "abc"
list1 = list(string)
high = len(list1)-1
permutation(list1,0,high)
