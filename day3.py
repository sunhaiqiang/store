from typing import List, Union

shop = [
    ["牙膏", 21.5],
    ["lenovo", 4500],
    ["Mac pro", 12000],
    ["Iphone 18 max Pro", 56000],
    ["海尔洗衣机", 2500],
    ["辣条", 3],
    ["洗衣粉", 25],
    ["利群", 160],
    ["红塔山", 130],
    ["机械革命", 8888]
]

mycart: List[Union[List[Union[str, float]], List[Union[str, int]]]] = []  # 空的购物车

# 初始化余额
salary = float(input("请输入您的钱包余额："))
salary: float
sal = salary = float(salary)
import random

coupo1 = random.randint(0, 10)  # 辣条的优惠卷
print("您有%d张辣条优惠卷三折" % coupo1)
a = 0.3
Threefold = float(a)
import random

coupo2 = random.randint(0, 20)  # 机械革命优惠卷
print("您有%d张机械革命优惠卷九折" % coupo2)
b = 0.9
ninefold = float(b)
while True:
    # 展示商品架
    for key, value in enumerate(shop):
        print(key, value)

    chose = input("请输入您要买的商品编号：")  # "9aa" --> 9
    if chose.isdigit():
        chose = int(chose)
        if chose == 5 and chose > 0:
            print("是否使用优惠卷")
            youhuijuan1 = input('请输入y或n')
            youhuijuan1: str
            if youhuijuan1 == "y":
                print("成功使用一张优惠卷")
                coupo1 -= 1
                salary -= (shop[chose][1] * 0.3)
                mycart.append(shop[chose])
                print(shop[chose][0], "添加购物车成功！余额还剩:￥", salary)
                print("还剩%d张优惠卷" % coupo1)
            else:
                if youhuijuan1 == "n":
                    salary = salary - shop[chose][1]
                    mycart.append(shop[chose])
                    print(shop[chose][0], "添加购物车成功！余额还剩:￥", salary)
                    print("还剩%d张优惠卷" % coupo2)
        elif chose == 9 and chose > 0:
            print("是否使用优惠卷")
            youhuijuan2 = input('请输入y或n')
            youhuijuan2: str
            if youhuijuan2 == "y":
                print("成功使用一张优惠卷")
                coupo2 -= 1
                salary -= (shop[chose][1] * 0.9)
                mycart.append(shop[chose])
                print(shop[chose][0], "添加购物车成功！余额还剩:￥", salary)
                print("还剩%d张优惠卷" % coupo2)
            else:
                if youhuijuan2 == "n":
                    salary = salary - shop[chose][1]
                    mycart.append(shop[chose])
                    print(shop[chose][0], "添加购物车成功！余额还剩:￥", salary)
                    print("还剩%d张优惠卷" % coupo2)
        else:
            if chose >= len(shop) and chose != 5 and chose != 9:
                    print("温馨提示：这个商品不存在！别瞎弄！")
            else:
                if salary < shop[chose][1]:
                    print("温馨提示：穷鬼，没钱，别瞎买！")
                else:
                    salary = salary - shop[chose][1]
                    mycart.append(shop[chose])  # 购物车
                    print(shop[chose][0], "添加购物车成功！余额还剩:￥", salary)
    elif chose == "q" or chose == "Q":
        print("欢迎下次光临！")
        break  # 跳出循环
    else:
        print("兄弟，商品不存在！别瞎弄！")

# 打印购物小条
print("----------------欢迎下次光临Jason小商店--------------")
print("以下是您的购物小条，请拿好：")
print("--------------------------------------------------")
m = []
for i in mycart:
    if i not in m:
        m.append(i)
        print(" %s x %s " % (i, mycart.count(i)))
    else:
        continue
k = '{:.2}'.format(sal - salary)
o = float(k)
print("-------------------------------------------------")
print("您本次还剩余额为：￥", salary, "，本次消费：￥", (o))
