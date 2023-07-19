# 1480. Running Sum of 1d Array
문제
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

풀이

입력 리스트를 for로 a에 각각 받는다.
sum에 a를 더한다.
더한 값은 새로운 리스트에 순서대로 추가해준다.
완성된 리스트를 리턴해준다.