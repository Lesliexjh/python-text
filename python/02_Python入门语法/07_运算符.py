"""
演示Python中的各类运算符
"""
#算术（数学）运算符
print("1+1=",1+1)
print("2-1=",2-1)
print("3*3=",3*3)
print("4/2=",4/2)
print("11//5=",11//5)
print("6%5=",6%5)
print("8**5=",8**5)

#赋值运算符
num=1+2*3
print(num)

#复合赋值运算符
# +=
num = 1
num +=1  #num=num + 1
print("num += 1",num)
num -=1
print("num -= 1",num)
num *=2
print("num *=2",num)
num /= 2
print("num /= 2",num)
num //= 2
print("num /= 2",num)
num %= 2
print("num %= 2",num)
num **= 2
print("num **= 2",num)
