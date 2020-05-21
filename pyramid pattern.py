n = 5
for i in range(n):
    print("\t" * (n-i),end = " ")
    for j in range(i+1):
        print("*", "\t"*2,end=" ")
    print("\n")