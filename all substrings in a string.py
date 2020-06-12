# def remove_same_element(result):
#     for i in result:
#         for j in result[result.index(i)+1:]:
#             if(i == j):
#                 result.remove(j)
#     return result
#
str = "muneef"
# result = [str[i:j] for i in range(len(str)) for j in range(i+1,len(str)+1)]
# # result = list(dict.fromkeys(result))
# result = remove_same_element(result)
# print(result)
result = []
for i in range(len(str)):
    for j in range(i+1,len(str)+1):
        if(str[i:j] not in result):
            result.append(str[i:j])
print(result)