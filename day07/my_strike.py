def getS(com,mine):
    ret = 0
    c1 = com[0:1]
    c2 = com[1:2]
    c3 = com[2:3]
    
    m1 = mine[0:1]
    m2 = mine[1:2]
    m3 = mine[2:3]
    
    if c1==m1: 
        ret += 1
    if c2==m2:
        ret += 1
    if c3==m3:
        ret += 1
    
    return ret

def getB(com,mine):
    ret = 0
    c1 = com[0:1]
    c2 = com[1:2]
    c3 = com[2:3]
    
    m1 = mine[0:1]
    m2 = mine[1:2]
    m3 = mine[2:3]
    
    if c1==m2 or c1==m3: 
        ret += 1
    if c2==m1 or c2==m3:
        ret += 1
    if c3==m1 or c3==m2:
        ret += 1
    
    return ret

def ranC():
    
    return "345"

com = ranC();
mine = "932"

s = getS(com,mine)
b = getB(com,mine)
print("s",s,"b",b)