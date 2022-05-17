class Solution:
    def myAtoi(self, s: str) -> int:
        result=0
        sign=1
        index=0
        n=len(s)
        
        int_max=pow(2,31)-1
        int_min=-pow(2,31)
        
        while index<n and s[index]==" ":
            index+=1
            
        
        if index<n and s[index]=="+":
            sign=1
            index+=1
        elif index<n and s[index]=="-":
            sign=-1
            index+=1
            
        while index<n and s[index].isdigit():
            digit=int(s[index])
            
            if (result>int_max//10) or (result==int_max//10 and digit>int_max%10):
                return int_max if sign==1 else int_min
            
            result=result*10+digit
            index+=1
            
        return sign*result