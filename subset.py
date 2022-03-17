def subset(num):
    num.sort()
    result=[[]]
    for i in num:
        result+=[s+[i] for s in result]
    return result


r=subset([1,2,3])
print(r)