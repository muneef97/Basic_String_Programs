def remove_duplicate(string):
    list1 = string.split()
    for i in range(len(list1)):
        for j in range(i+1,len(list1)-1):
            if(list1[i]==list1[j]):
                list1.remove(list1[j])
    return " ".join(list1)

string = "java java jav"
result = remove_duplicate(string)
print(result)