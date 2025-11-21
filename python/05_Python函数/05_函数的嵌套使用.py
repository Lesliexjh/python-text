"""
演示嵌套调用函数
"""

def add(x,y):
    z=x+y
    print(f"和为{x}+{y}={z}")
    return z
def subtract(x,y):
    z=x-y
    print(f"差为{x}-{y}={z}")
    add(x,y)
    return z

subtract(10,1)