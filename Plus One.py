from ast import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        b=""
        for i in digits:
            b+=str(i)
        b=str(int(b)+1)
        c=[int(j) for j in b]
        return c
                
                
