# 412. Fizz Buzz
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.

풀이
for문과 if문을 이용해 3과 5로 나뉘면 "FizzBuzz", 3으로만 나뉘면 "Fizz", 5로만 나뉘면 "Buzz"을 list에 입력한다. 3과 5로 나누어지지않는다면 숫자를 리스트에 입력
리스트를 출력
