"""

写一个判断是否为三角形他函数parseTrigon(a,b,c)
语言优先使用python>java>c>其他
入参：a,b,c三个字符串代表三边，要求在函数内部判断各边长均为1~10的整数。
返回值：有四种可能：
1.边长不合法（非三角形，即存在两边之和大于第三边）
2.普通三角形
3.等边三角形
4.等腰三角形
"""

a: int=int(input("请输入三角形边长"))
if 0 >= a or a > 10:
    print("请输入1~10的整数")
else:
    b: int=int(input("请输入三角形边长"))
    if 0 >= b or b > 10:
        print("请输入1~10的整数")
    else:
        c: int=int(input("请输入三角形边长"))
        if 0 >= c or c > 10:
            print("请输入1~10的整数")
        else:
            if a+b>c and a+c>b and b+c>a:
                if a == b and a!=c or a == c and a!=b or b == c and a!=b:

                        print("等腰三角形")

                elif a==b==c:
                    print("等边三角形")
                else:
                    print("普通三角形")
            else:
                print("边长不合法")



