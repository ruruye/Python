# 첫수를 입력하시오 1
# 끝수를 입력하시오 10
# 배수를 입력하시오 5
# 1에서 10까지 5의배수의 합은 15입니다.

start = input("첫수를 입력하시오")
end = input("끝수를 입력하시오")
c = input("배수를 입력하시오")

aa = int(start)
bb = int(end)
cc = int(c)

sum = 0
for i in range(aa,bb+1):
    if i%cc == 0:
        sum += i


print("{}에서 {}까지 {}의 배수의 합은 {}입니다".format(start,end,c,sum))





