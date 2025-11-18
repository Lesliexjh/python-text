# import random
# num=random.randint(1,10)
# print("让我们开始猜数字！")
# print(num)
# num1=int(input("猜第一次"))
# if num1==num:
#     print("猜对了")
# elif num1>num:
#     print("猜大了")
#     num2 = int(input("猜第二次"))
#     if num2==num:
#         print("猜对了")
#     elif num2>num:
#         print("又猜大了")
#         num3=int(input("猜第三次"))
#         if num3==num:
#             print("猜对了")
#         else:
#             print(f"又猜错了，实际结果是{num}")
#     else:
#         print("猜小了")
#         num3=int(input("猜第三次"))
#         if num3 == num:
#             print("猜对了")
#         else:
#             print(f"又猜错了，实际结果是{num}")
# else:
#     print("猜小了")
#     num2 = int(input("猜第二次"))
#     if num2 == num:
#         print("猜对了")
#     elif num2 > num:
#         print("猜大了")
#         num3 = int(input("猜第三次"))
#         if num3 == num:
#             print("猜对了")
#         else:
#             print(f"又猜错了，实际结果是{num}")
#     else:
#         print("又猜小了")
#         num3 = int(input("猜第三次"))
#         if num3 == num:
#             print("猜对了")
#         else:
#             print(f"又猜错了，实际结果是{num}")



import random
num=random.randint(1,10)
print("让我们开始猜数字！")
print(num)
num1=int(input("猜第一次"))
if num1==num:
    print("猜对了")
else:
    if num1<=num:
        print("猜小了")
    else:
        print("猜大了")
    num2=int(input("猜第二次"))

    if num2 == num:
        print("猜对了")
    else:
        if num2 <= num:
            print("猜小了")
        else:
            print("猜大了")

        num3 = int(input("猜第三次"))
        if num3 == num:
            print("猜对了")
        else:
            if num3 <= num:
                print("猜小了")
            else:
                print("猜大了")

#text