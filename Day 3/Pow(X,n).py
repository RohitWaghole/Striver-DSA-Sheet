class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n>0:
            ans=1
            for i in range(n):
                ans*=x
        elif n==0: return 1
        else:
            ans=1
            for i in range(abs(n)):
                ans/=x
        return ans

########################################################################

class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n

########################################################################

class Solution:
    def myPow(self, x: float, n: int) -> float:
        return math.pow(x,n)

########################################################################

class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        f = 0
        if n<0:
            n *= -1
            f = 1
            
        ans = 1
        
        while n>0:
            
            if n%2==1:
                ans *= x
                n -= 1
            else:
                x *= x
                n //= 2
                
        if f:
            return 1/ans
        return ans
