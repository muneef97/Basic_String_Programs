def max_char(string):
    result = {}
    for i in string:
        result[i]=string.count(i)
    print(max(result, key=result.get))


string = 'muneef'
max_char(string)
