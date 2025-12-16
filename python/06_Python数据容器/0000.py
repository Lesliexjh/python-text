def suma2b(a,b):
    while a<=b:
        sum=a+a+1
        a+=a
    return sum
print(suma2b(2,5))


def gcd(m, n):
    """求 m 和 n 的最大公约数（欧几里得算法）"""
    m = abs(m)
    n = abs(n)
    while n != 0:
        m, n = n, m % n
    return m

def lcm(m, n):
    """求 m 和 n 的最小公倍数"""
    return abs(m * n) // gcd(m, n)

# ===== 调用函数 =====
a = int(input("请输入第一个整数: "))
b = int(input("请输入第二个整数: "))

g = gcd(a, b)
l = lcm(a, b)

print(f"{a} 和 {b} 的最大公约数 GCD = {g}")
print(f"{a} 和 {b} 的最小公倍数 LCM = {l}")
