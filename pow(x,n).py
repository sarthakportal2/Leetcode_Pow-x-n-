class Solution:
    def myPow(self, x: float, n: int) -> float:
        #min. runtime(27 ms) T(C(N)=O(log(n)) and S(C(N)=O(log(n))) as it requires contigous memory allocation at (n-(-1*n/x)) at half recursion
        if n<0:x=1/x;n=-1*n#converting (-ve) exponential power into (+ve) Power
        out=1#outPut Val Declare
        while n>0:#positive Number Iteration
            if n&1:#ing output 's power to 1 Declare
                out=out*x#output's square 
            n>>=1#power's Right Shift declare
            x=x*x#power's square 
        return out#printing the output
