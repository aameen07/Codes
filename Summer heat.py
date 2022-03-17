T=int(input())
for _ in range (T):
    xa, xb, Xa, Xb = input().split()
    total = (int(Xa)//int(xa))+int(int(Xb)//int(xb))
    print (total)


or

#import math
#t=int(input())
#for i in range(t):
#    sxa,sxb,xa,xb=map(int,input().split())
#    print(math.ceil(xa/sxa)+math.ceil(xb/sxb))