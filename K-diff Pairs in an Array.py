from ast import List


class Solution:
    def findPairs(self, num: List[int], k: int) -> int:
        
        count=0
        d={}
        for i in num:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        if k==0:   
            for i in set(num):
                if d[i]>=2:
                    count+=1
                    
        else:
            nums=set(num)
            for i in nums:
                a=i-k
                if a in d:
                    count+=1
        return count
        
        
 
        
        
#         count=0
#         for i in range (len(num)):
#             for j in range(i+1,len(num)):
#                 if ((num[i]-num[j])==k) or ((num[i]-num[j])==-k):
#                     count+=1                 
#         return count
                