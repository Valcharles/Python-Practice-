a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
x =[]
num=int(input('Enter a number')) #get number from user 
for i in a:
    if i < num:
        x.append(i)
print(x)
