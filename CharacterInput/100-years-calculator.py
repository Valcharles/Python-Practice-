#Collect necessary data from user
username= input('Enter your name')
age = int(input('Enter your current age'))

#Compute and process input 
year100= 2022 + (100 - age)

#output result
print ('{} will be 100 years in {}'.format(username,year100))

#Extras
#print out n copies of result
n= int(input('how many copies do you want?'))
ctr = 0
while ctr < n:
    print ('{} will be 100 years in {}'.format(username,year100))
    ctr +=1
    
#Print n copies each on a new line. 
while ctr < n:
    print ('{} will be 100 years in {}\n'.format(username,year100))
    ctr +=1
