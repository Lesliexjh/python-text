def sum_xy(x,y):
    sum=x+y
    print(f'{x}+{y}={sum}')
    return sum

sum_xy(1,2)

def wen(x):
    if 36<x<36.7:
        print(f"体温{x}，正常")
    else:
        print("不正常")

wen(float(input()))