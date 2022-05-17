from ast import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=matrix
        for r in range(len(m)):
            for c in range(r,len(m)):
                
                m[r][c],m[c][r]=m[c][r],m[r][c]
                
        for r in range(len(m)):
            
            m[r]=m[r][::-1]