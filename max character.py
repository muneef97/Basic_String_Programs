# def max_char(string):
#     result = {}
#     for i in string:
#         result[i]=string.count(i)
#     print(max(result, key=result.get))
#
#
# string = 'muneef'
# max_char(string)

string = 'aabb'
maximum = 0
result = ''
for i in range(len(string)) :
    count = 0
    for j in range(i+1,len(string)):
        if(string[i] == string[j]):
            count += 1
    if(count > maximum):
        maximum = count
        result = string[i]
print(result)