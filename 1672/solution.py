class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sumlist = []
        for a in accounts:
            sum = 0
            for b in a:
                sum = sum + b
            sumlist.append(sum)

        #기준값을 리스트 첫번째 값으로
        x=sumlist[0]

        for c in sumlist:
            if(c>=x):
                x=c

        return x