num=10000
no=1
import random
for no in range(1,21):
    if num>0:
        cont = random.randint(1, 10)
        if cont<5:
            print(f'{no}不配')
        else:
            num=num-1000
            print(f'{no}领了1000块大洋，剩余{num}元')
    else:
        break

num=10000
no=1
import random
for no in range(1,21):
    cont = random.randint(1, 10)
    if num>0 and cont>5:
        num=num-1000
        print(f'{no}领了1000块大洋，剩余{num}元')
    else:
        print(f'{no}不配')
