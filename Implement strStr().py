class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = haystack_length = len(haystack)
        n = needle_length = len(needle)
        
        extra_length = p = m-n+1
        #this is the length which is extra in the string so we use this in the loop
        
        if n==0:
            return 0
        for i in range (p) :
            if haystack[i:i+n]==needle:
                return i     
        return -1