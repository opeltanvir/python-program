import math

user_num = int(input("Upper linit fit prime: "))


def is_prime(num):
    for i in range(2,int(math.sqrt(num) +1 )):
       if num % i == 0:
         return false
    return true


for i in range(1, user_num + 1):
    if is_prime(i):
        print(i)