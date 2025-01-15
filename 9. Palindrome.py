class Solution:
    def isPalindrome(self, x: int) -> bool:
        #return str(x) == str(x)[::-1] , for string
        org_num=x
        z= 0
        if x < 0:
            return False
        else:
            while(x > 0):
                y = x % 10
                z= z*10 + y
                x= x // 10
            return org_num == z
        
