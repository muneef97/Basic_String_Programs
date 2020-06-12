def convert(str1):
    if (str1[-2:]=="AM" and str1[:2]=="12"):
        return ("00"+str1[2:-2])
    elif (str1[-2:]=="AM"):
        return (str1[:-2])
    elif (str1[-2:]=="PM" and str1[:2]=="12"):
        return ("12"+str1[2:-2])
    else:
        return (str(int(str1[:2])+12)+str1[2:-2])
str1 = "02:15:45 PM"
result = convert(str1)
print(result)