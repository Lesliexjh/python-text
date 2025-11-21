"""
函数的文档说明
:param x:形参x的说明
:parma y:形参y的说明
:return:
"""

def add(x,y):
    """
    add函数可以接受2个参数，进行2数相加求和
    :param x:形参x 表示第一个加数
    :param y:形参y 表示第二个加数
    :return:返回2数相加结果
    """
    result = x + y
    print(f"{x} + {y} = {result}")
    return result

add(1,2)