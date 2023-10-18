# 1~45까지 수 중에서 로또만드세요

from random import random

arr = list(range(1,45+1))

for i in range(1000):
    r = int(random()*45)
    a = arr[0];
    arr[0]=arr[r]
    arr[r]=a

print(arr[0:6])

