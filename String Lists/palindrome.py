a= list(input('Enter a word'))
ctr=len(a)-1
tmp=[]
for i in a:
    tmp.append(a[ctr])
    ctr= ctr-1
#print(tmp)
#print(a)
if a==tmp:
    print('Your word is a palindrome')
else:
    print('Your word is not a palindrome')
