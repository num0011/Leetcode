##Example 1:

#Input: nums = [1,2,3,4]
#Output: [1,3,6,10]
#Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum=0
        sumlist=[]
        for a in nums:
            sum = sum + a
            sumlist.append(sum)

        return sumlist