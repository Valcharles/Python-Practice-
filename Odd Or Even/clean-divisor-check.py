#Get Data from User 
num= int(input('Enter  numerator'))
check= int(input('Enter denominator'))

#Process & Display result
if num % check == 0:
  print (str(num) + ' is a multiple of ' + str(check))
else:
   print (str(num) + ' is not a multiple of ' + str(check))
