from ast import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        result=[[]]
        for i in nums:
            result+=[s+[i] for s in result]
        return result

