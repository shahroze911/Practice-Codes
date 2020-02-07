x=int(input("Starting Table: "))
y=int(input("Ending Table: "))
for i in range(x,y+1):
    for j in range(1, 11):
        n = i * j
        x=i
        print(x, "*", j, "=", n)
    print("*"*15)





