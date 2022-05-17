from ast import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
                
        for i in nums:
            while d[i]>2:
                nums.remove(i)
                d[i]-=1
                
                