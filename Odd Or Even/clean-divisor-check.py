#Get Data from User 
num= int(input('Enter  numerator'))
check= int(input('Enter denominator'))

#Process & Display result
if num % check == 0:
  print (str(check) + ' is a clean divisor of ' + str(num))
else:
   print (str(check) + ' is not a clean divisor of ' + str(num))
