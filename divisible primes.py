def sumOfNumber(num):   #this function sums the terms of the number
    s = 0
    while(num > 0):
        rem = num % 10
        s += rem
        num = num // 10
    return s

def isPrime(num):       #this checks prime  
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def findDivisiblePrimeCount(a, b, n):
    count = 0
    for num in range(a, b+1):
        if isPrime(num) and (sumOfNumber(num) % n ==1):
            count += 1
    return count

a=int(input("enter a"))
b = int(input("enter b"))
n = int(input("enter n"))
count=findDivisiblePrimeCount(a,b,n)
print(count)