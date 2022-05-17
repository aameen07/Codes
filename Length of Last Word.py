class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        li=s.split()
        if li!=[]:
            return (len(li[-1]))
        return 0