'''Write a program which inputs two numbers (which will be less than 10,000) and then prints "Amicable" if they are amicable, 
or "Not amicable" otherwise. Your program should then terminate. (20 marks)
'''
import sys


def divisors(n):
    result = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            result.add(i)
            result.add(n//i)
    return list(result)



print("input number 1")
num1= int(input())
if num1 >10000:
    sys.exit()
print("input number2")
num2 = int(input())
if num2 > 10000:
    sys.exit()
    
        
        
num1d = divisors(num1)

num2d = divisors(num2)

total1 = 0
total2 = 0
for i in range(len(num1d) - 1):
    total1 += i
for i in range(len(num2d) - 1):
    total2 += i
    
    
if total1 == num2 or total2 == num1:
    print('amicable')
    sys.exit()
else:
    print("not amicable")
    sys.exit()
    
