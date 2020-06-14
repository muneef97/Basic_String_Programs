string1 = 'ababab'
result = ''
count = 0
for i in range(len(string1)):
    if(len(string1) != i+1 and string1[i]==string1[i+1]):
        count += 1
    else:
        result = result + str(count+1) + string1[i]
        count = 0
print(result)