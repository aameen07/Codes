# cook your dish here
t = int(input())
for _ in range(t):
    n = str(input())
    sum = 0
    first_digit = int(n[0])
    last_digit = int(n[-1])
    sum = first_digit + last_digit
    print(sum)
    