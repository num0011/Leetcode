#Example 1

#Input: num = 14
#Output: 6
#Explanation: 
#Step 1) 14 is even; divide by 2 and obtain 7. 
#Step 2) 7 is odd; subtract 1 and obtain 6.
#Step 3) 6 is even; divide by 2 and obtain 3. 
#Step 4) 3 is odd; subtract 1 and obtain 2. 
#Step 5) 2 is even; divide by 2 and obtain 1. 
#Step 6) 1 is odd; subtract 1 and obtain 0.

class Solution:
    def numberOfSteps(self, num: int) -> int:
        n=num
        h=0
        while True:
            if n/2==0:
                break
            elif n%2!=0:
                h=h+1
                n=n-1
            elif n%2==0:
                h=h+1
                n=n/2
        return h