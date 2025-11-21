money=10000

def cha():
    print(f"当前余额为{money}")

def cun():
    global money
    x=int(input("输入存款金额："))
    money=x+money
    print(f"存款成功当前余额为{money}")

def qu():
    global money
    x=int(input("请输入取款金额："))
    money=money-x
    print(f"取款成功，当前余额为{money}")

pass_word = input("请输入密码：")
if pass_word == "109928":
    print("welcome Leslie")
    while True:
        x=input("请问你要干什么？\n查询输入1\n存款输入2\n取款输入3\n")
        if x=="1":
            cha()
        if x=="2":
            cun()
        if x=="3":
            qu()
        if x=="4":
            break
else:
    print("密码错误")