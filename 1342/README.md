#1342. Number of Steps to Redu

문제
Given an integer num, return the number of steps to reduce it to zero.
In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

풀이
적기 쉽게 입력받은 num을 n에 저장한다.
몇번 계산이 진행됐는지 세는 h를 선언한다.
while문을 통해 2로 나누었을때 0이되면 while문을 break로 빠져나온다
2로 나누었을때 나머지가 0이 아니면 짝수가 아니므로 n에서 1을 빼고 다시 n에 저장하고 계산한 횟수(h)를 올린다.
2로 나누었을때 나머지가 0이면 짝수이므로 n에서 2로 나눈 몫을 다시 n에 저장하고 계산한 횟수(h)를 올린다.
while문을 빠져나오면 계산된 횟수를 반환한다.