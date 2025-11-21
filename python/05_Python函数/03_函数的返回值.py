def sum(x,y):
    z=x+y
    return z

print(f"{sum(3,4)}")


def Nian(x):
    if x>=18:
        return "成年"
    else:
        return "未成年"

print(Nian(int(input("输入年龄"))))