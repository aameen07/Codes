n=int(input())
dic={}
for _ in range(n):
    name, *line= input().split()
    score=list(map(float,line))
    dic[name]=score
qname=input()
marks=dic[qname]
#format(value,'.nf')
print(format(sum(marks)/3, '.2f'))