def anagram(str1,str2):
    if(len(str1)!=len(str2)):
        return -1
    else:
        list1 = list(str1)
        list2 = list(str2)
        for i in range(len(list1)):
            j = 0
            while (j < len(list2)):
                if(list1[i]==list2[j]):
                    list2.remove(list2[j])
                j += 1
        if(len(list2)== 0):
            return 1
        else:
            return -1

str1 = "enefum"
str2 = "muneef"
result = anagram(str1,str2)
if(result == 1):
    print("Anagram")
else:
    print("Not anagram")