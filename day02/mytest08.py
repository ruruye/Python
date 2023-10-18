# 출력할 구구단을 입력하세요 7
# 7*1=7
# 7*9=63

gugu = input("출력할 구구단을 입력하세요")
igugu = int(gugu)

for i in range(1,9+1):
    print("{}*{}={}".format(gugu,i,i*igugu))

# print("{}*{}={}".format(gugu,1,1*igugu))
# print("{}*{}={}".format(gugu,2,2*igugu))
# print("{}*{}={}".format(gugu,3,2*igugu))
# print("{}*{}={}".format(gugu,4,2*igugu))
# print("{}*{}={}".format(gugu,5,2*igugu))
# print("{}*{}={}".format(gugu,6,2*igugu))
# print("{}*{}={}".format(gugu,7,2*igugu))
# print("{}*{}={}".format(gugu,8,2*igugu))
# print("{}*{}={}".format(gugu,9,2*igugu))
