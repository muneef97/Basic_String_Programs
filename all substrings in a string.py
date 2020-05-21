str = "muneef"
result = [str[i:j] for i in range(len(str)) for j in range(i+1,len(str)+1)]
result = list(dict.fromkeys(result))
print(result)