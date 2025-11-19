import random
num=random.randint(1,100)
y=True
z=0
while y:
    z=z+1
    x=int(input("请猜第%d次"%z))
    if x==num:
        print("猜中了")
        break
    elif x>num:
        print("大了")
    else:
        print("小了")
print("你猜了%d次"%z)