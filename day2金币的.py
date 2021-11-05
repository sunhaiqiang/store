import random

a = random.randint(0, 150)
A = 1
B = 5000
C = 500
D = 3000
print("初始金币", B)
for A in range(20):
    b = int(input('请输入数字：'))
    if b > a:
        print("输入的大了哦")
        B = B - C
        print(B, "现有金币")
    elif b < a:
        print("输这么小干嘛")
        B = B - C
        print(B, "现有金币")
    else:
        print("很幸运猜对了")
        B = B + D
        print(B, "现有金币")
        break
    if B < 0:
        break
