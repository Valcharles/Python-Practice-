import random
randomlist1=random.sample(range(1,100), 10)
randomlist2=random.sample(range(1,100),15)
x=[]
for i in randomlist2:
     if i in randomlist1:
         x.append(i)
print(randomlist1) 
print(randomlist2)
print(x)
