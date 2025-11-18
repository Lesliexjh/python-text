a="apple"
b="000001"
c=100
print(f"公司{a}股票代码{b}当前股价{c}")
print("公司%s，股票代码%s，当前股价%.2f" % (a,b,c))
print("7天后股价为%.2f"%(c*(1.2**7)))
n=int(input("几天后"))
print("%i天后股价为%.2f" %(n,c*(1.2**n)))