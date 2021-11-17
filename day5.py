import random


bank = {}
# 银行名称
bank_name = "中国农业银行昌平支行"


def welcome():
    print("---------------------------------------")
    print("-     中国农业银行账户管理系统V1.0      -")
    print("---------------------------------------")
    print("-  1.开户                             -")
    print("-  2.存钱                             -")
    print("-  3.取钱                             -")
    print("-  4.转账                             -")
    print("-  5.查询                             -")
    print("-  6.Bye!                             -")
    print("--------------------------------------")


# 银行的开户逻辑
def bank_addUser(account, account_type, name, password, country, province, street, door, money):
    if len(bank) > 100:
        return 3

    if name in bank:
        return 2

    # 正常开户
    bank[name] = {
        # "name": str(name),  # 用户名
        "account": str(account),  # 账户
        "account_type": int(account_type),  # 账户类型
        "password": str(password),  # 密码
        "country": str(country),  # 国际
        "province": str(province),  # 省份
        "street": str(street),  # 街道
        "door": str(door),  # 门牌号
        "money": 0,  # 金额
        "bank_name": str(bank_name)  # 银行
    }
    return 1


# 开户的输入数据
def addUser():
    name = input("请输入姓名：")

    account_type = input('''
    请输入账户类型
    一类卡：金卡，输入1；
    二类卡：普通卡，输入2
                         ''')

    password = input("请输入密码：")

    country = input("请输入国籍：")

    province = input("请输入省份：")

    street = input("请输入街道：")

    door = input("请输入您家门牌号：")

    money = 0

    account = random.randint(10000000, 99999999)

    status = bank_addUser(name, account_type, password, country, province, street, door, money, account)

    if status == 3:
        print("对不起，该银行用户已满，请携带证件到其他银行办理！")
    elif status == 2:
        print("您之前已经开过户！禁止重复开户！")
    elif status == 1:
        print("嘻嘻，开户成功！以下卡户的个人信息：")
        info = '''
            ------------个人信息查询结果-------------
            用户名：%s
            账号：%s
            密码：%s
            账户类型：%s
            地址：
                国籍：%s
                省份：%s
                街道：%s
                门牌号：%s
            余额：%s
            开户行名称：%s
            ---------------------------------------
        '''
        print(info % (name, account, password, account_type, country, province, street, door, money, bank_name))


# 定义存钱

def saveadd(name):
    if name in bank:
        print("您的余额为：%d" % bank[name]["money"])
        money = int(input("请输入您要存入的金额：")) + bank[name]["money"]
        bank[name]["money"] = money
        return True
    else:
        return False


# 定义取钱
def withdrawaladd(name, password):
    if name in bank and password == bank[name]["password"]:

        print("您的余额为%d" % bank[name]["money"])

        money = bank[name]["money"] - int(input("请输入您要取款的金额："))

        if money >= 0:
            bank[name]["money"] = money
            return 0
        elif money < 0:
            return 3
    elif name not in bank:
        return 1
    elif name in bank:
        if password != bank[name]["password"]:
            return 2


# 定义转账
def transferadd(zhuanru_name, zhuanchu_name, password,account_type):

    if zhuanru_name in bank and zhuanchu_name in bank:
        zhuanchu_money = int(input("请输入您要转账的金额："))
        if password == bank[zhuanru_name]["password"]:

            if bank[zhuanru_name]["account_type"] == 2:
                print("您的账户类型为金卡，转出最大额度2万")
            elif zhuanchu_money > 20000:
                print("您的额度不足")
                return 3
            if bank[zhuanchu_name]["account_type"] == 1:
                print("您的账户类型为金卡，转出最大额度5万")
            elif zhuanchu_money > 50000:
                print("您的额度不足")
                return 3
            if bank[zhuanchu_name]["account_type"] != 1 or bank[zhuanchu_name]["account_type"] != 2:
                print("没有改账户类型")
                return 1
        money = bank[zhuanchu_name]["money"] - zhuanchu_money
        if money >= 0:
            bank[zhuanchu_name]['money'] = money
            bank[zhuanru_name]['money'] = zhuanchu_money + bank[zhuanru_name]['money']
            return 0
        elif money < 0:
            return 3

    elif password != bank[zhuanru_name]['password']:
        return 2
    else:
        return 1


# 定义查询
def inquireadd(name, password):
    if name in bank and password == bank[name]["password"]:
        return 1
    else:
        return 0


# 存钱的数据

def cqadd():
    name = input("请输入您的用户名：")
    cq = saveadd(name)
    if cq:
        info = '''
                ------------个人信息------------
                用户名:%s
                密码：*****
                余额：%s
                开户行名称：%s
        '''
        # 每个元素都可传入%
        print(info % (name, bank[name]["money"], bank_name))
    elif not cq:
        print("用户名无效")


# 取钱的数据
def qqAdd():
    name = input("请输入您的用户名：")
    password = input("请输入您的密码：")
    qq = withdrawaladd(name, password)


    if qq == 1:
        print("账号不存在")
    elif qq == 2:
        print("密码输入错误")
    elif qq == 3:
        print("账号余额不足")
    elif qq == 0:
        info = '''
               ------------个人信息------------
               用户名:%s               
               密码：*****
               余额：%s
               开户行名称：%s
           '''
        # 每个元素都可传入%
        print(info % (name, bank[name]["money"], bank_name))


# 转账的数据

def zzadd():
    zhuanru_name = input("请输入您要转出的账户：")
    password = input("请输入您的用户密码：")
    zhuanchu_name = input("请输入您要转入的账户：")
    account_type = bank[zhuanchu_name]["account_type"]
    zz = transferadd(zhuanchu_name, zhuanru_name, password,account_type)

    if zz == 1:
        print("转出或转入的账号不存在或账户类型不存在")
    elif zz == 2:
        print("转出账户的密码输入错误")
    elif zz == 3:
        print("转出账户的余额不足或额度不足")
    elif zz == 0:
        info = '''
               ------------个人信息------------
               用户名:%s
               账户类型：%s               
               密码：*****
               余额：%s
               开户行名称：%s
           '''
        # 每个元素都可传入%
        print(info % (zhuanru_name, bank[zhuanru_name]["account_type"],bank[zhuanru_name]["money"], bank_name))
        info = '''
               ------------个人信息------------
               用户名:%s
               账户类型：%s               
               密码：*****
               余额：%s
               开户行名称：%s
           '''
        # 每个元素都可传入%
        print(info % (zhuanchu_name,bank[zhuanchu_name]["account_type"], bank[zhuanchu_name]["money"], bank_name))



# 查询

def cxAdd():
    name = input("请输入您的用户名：")
    password = int(input("请输入您的用户密码："))
    cx = inquireadd(name, password)

    if cx == 1:
        print("账户信息不存在")
    elif cx == 2:
        print("密码输入错误")
    elif cx == 0:
        info = '''
                              ------------个人信息------------
                              用户名:%s
                              账户类型：%s
                              账号：%s
                              密码：%s
                              国籍：%s
                              省份：%s
                              街道：%s
                              门牌号：%s
                              余额：%s
                              开户行名称：%s
                          '''
        # 每个元素都可传入%

        print(info % (name, bank[name]['account_type'], bank[name]['account'], bank[name]['password'],
                      bank[name]['country'], bank[name]['province'],
                      bank[name]['street'], bank[name]['door'], bank[name]["money"], bank_name))


while True:
    welcome()
    chose = input("请输入业务编号：")
    if chose == "1":
        print("开户")
        addUser()
    elif chose == "2":
        print("存钱")
        cqadd()
    elif chose == "3":
        print("取钱")
        qqAdd()
    elif chose == "4":
        print("转账")
        zzadd()
    elif chose == "5":
        print("查询")
        cxAdd()
    elif chose == "6":
        print("Bey!")
        break
