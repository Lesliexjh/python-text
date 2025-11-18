"""
演示if elif else 多条件判断语句的使用
"""

"""
if int(input("请输入身高"))<=160:
    print("免票")
elif int(input("输入vip等级"))>=3:
    print("免票")
else:
    print("买票")
"""
#练习
a=int(input("我想的数字"))
if int(input("猜一次"))==a:
    print("猜对了")
elif int(input("猜两次"))==a:
    print("猜对了")
elif int(input("猜三次"))==a:
    print("猜对了")
else:
    print(f"我想的是{a}")
    print("想的是%s"%a)

