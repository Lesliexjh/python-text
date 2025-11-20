from tokenize import endpats

i=1
for i in range(1,101):
    j=1
    for j in range(1,11):
        print(f"第{j}朵花")
        j=i+1
    print(f"第{i}天Leslie,I love u")
    i=i+1
print("成功")


i=j=1
for i in range(1,10):
    for j in range(i,10):
        print(f"{i}*{j}={i*j}",end="\t")
        j=j+1
    print()