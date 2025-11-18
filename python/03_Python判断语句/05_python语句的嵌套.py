"""
演示判断语句的嵌套使用
"""
"""
if int(input("输入身高"))>=160:
    if int(input("请输入vip"))>=3:
        print("免费")
    else:
        print("10块")
else:
    print("免费")
"""

"""
练习
"""
if 18<=int(input("输入年龄"))<=30:
    if int(input("入职时间"))<=2:
        if int(input("vip"))>=3:
            print("有奖")
        else:
            print("无")
    else:
        print("有奖")
else:
    print("无")