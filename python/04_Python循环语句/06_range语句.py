#range语法1   range(num)
range(10)
for i in range(10):
    print(i)

#range语法   range(num1,num2)
for i in range(5,10):
    print(i)

#range语法   range(num1,num2,step)
for i in range(5,10,2):
    print(i)

num=0
for i in range(1,100):
    if i%2==0:
        num=num+1
print(num)
