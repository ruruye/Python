# 첫수를 입력하세요 7 9
# 7은 9보다 2만큼 작다

# 끝수를 입력하세요 9 7
# 9는 7보다 2만큼 크다

# 끝수를 입력하세요 8 8
# 같은 숫자 입니다

a = input("첫수를 입력하세요")
b = input("끝수를 입력하세요")

if a < b:
    diff = int(b) - int(a)
    print("{}는 {}보다 {}만큼 작다".format(a,b,diff))
elif a > b:
    diff = int(a)-int(b) 
    print("{}는 {}보다 {}만큼 크다".format(a,b,diff)) 
else:
    print("같은숫자입니다")







