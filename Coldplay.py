""" T=int(input())
for i in range(T): 
    m,s = input().split()
    journey_time = m = int(m)
    song_time_ = s = int(s)
    count=0
    if(s>m):
        print('0')
        continue
    while(s<=m):
        if (s<=m):
            count+=1
            m=m-s
        else:
            break
    print(count)
 """
#or

tc = int(input())

for _ in range(tc):
    m, s = map(int, input().split())
    print(m // s)
