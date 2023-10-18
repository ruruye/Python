# 1에서 9까지 수 중에서 중복없이 섞어서 3개의 수를 출력하세요
from random import random

arr = [1,2,3,4,5,6,7,8,9]

for i in range(99):
    r = int(random()*9)
    a = arr[0];
    arr[0]=arr[r]
    arr[r]=a

print(arr[0],arr[1],arr[2])

