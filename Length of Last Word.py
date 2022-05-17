s="  my name is khan  "
s=s[::-1]
start=0
for c in s:
    if c!=' ':
        break
    start+=1

pos=s.find(' ',start)
if pos<0:
    print (len(s) - start if start<len(s) else 0)
print (pos-start)