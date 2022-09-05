def is_prime(num):
    factors=[]
    for i in range(2,num):
        if num%i == 0:
            factors.append(i)
    if len(factors) == 0:
        print('{} is a prime number'.format(num))
    else:
        print('{} is not a prime number'.format(num))
        print('Some factors of {} :{}'.format(num,factors))
