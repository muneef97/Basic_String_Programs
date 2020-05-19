def remove_duplicate(string):
    list = string.split()
    for i in range(len(list)):
        for j in range(i+1,len(list)-1):
            if(list[i]==list[j]):
                list.remove(list[j])
    return " ".join(list)

string = "java java jav"
result = remove_duplicate(string)
print(result)