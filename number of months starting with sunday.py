def isleapyear(year):
    if(year%100 ==0 and year%400 == 0):
        return True
    elif(year%4==0 and year%100!=0):
        return True
    else:
        return False

year = 1900
year_range =10
total_months = year_range * 12
day = 1
true_count = 0
for i in range(total_months):
    if((i%12<=6 and i%2 == 0) or (i%12 >6 and i%2 != 0)):
        day = (day + 3)%7
    elif(i%12 == 1):
        if(isleapyear(year)==True):
            day = (day + 3)%7
    else:
        day = (day + 3)%7
    if(day%7 == 0):
        true_count += 1
    if(i>0 and i%12==0):
        year += 1
print(true_count)

