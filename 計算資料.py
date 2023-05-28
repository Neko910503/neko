arr = input("Please input a series of numbers: 剪刀(1) 石頭(2) 布(3):")
arr = [int(n) for n in arr.split()] #分割字串

S=0
R=0
P=0
SS=0
SR=0
SP=0
RS=0
RR=0
RP=0
PS=0
PR=0
PP=0

for a in range(len(arr)):
    if arr[a]==1:
        S=S+1
    if arr[a]==2:
        R=R+1
    if arr[a]==3:
        P=P+1
    if a!=401:
        if arr[a]==1:
            if arr[a+1]==1:
                SS=SS+1
            if arr[a+1]==2:
                SR=SR+1
            if arr[a+1]==3:
                SP=SP+1
        if arr[a]==2:
            if arr[a+1]==1:
                RS=RS+1
            if arr[a+1]==2:
                RR=RR+1
            if arr[a+1]==3:
                RP=RP+1
        if arr[a]==3:
            if arr[a+1]==1:
                PS=PS+1
            if arr[a+1]==2:
                PR=PR+1
            if arr[a+1]==3:
                PP=PP+1

print('\n統計: 剪刀{} 石頭{} 布{} 共{}局'.format(S,R,P,S+R+P))
print('\n剪刀後: 剪刀{} 石頭{} 布{} 共{}'.format(SS,SR,SP,SS+SR+SP))
print('\n石頭後: 剪刀{} 石頭{} 布{} 共{}'.format(RS,RR,RP,RS+RR+RP))
print('\n布後: 剪刀{} 石頭{} 布{} 共{}'.format(PS,PR,PP,PS+PR+PP))