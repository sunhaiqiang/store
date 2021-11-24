import xlrd


baidu = xlrd.open_workbook(filename=r"G:\pythonProject1\学习所创建的文件夹\测试组\day7\百度合作单位-人员管理-二期.xls")
st = baidu.sheet_by_index(0)
rows = st.nrows
cols = st.ncols
nan = 0
nv = 0
nianling = 0
money1 = 0
money2 = 0
phone1 = 0
phone2 = 0
phone3 = 0
heilongjiang = 0
beijin = 0
fujian = 0
sichuan = 0
gongsi = 0
for j in range(1,rows):
    data = st.row_values(j)
    if data[8] == "男":
        nan = nan + 1
    elif data[8] =="女":
        nv = nv + 1
    if data[7] > 45:
        nianling = nianling + 1
    if data[11] > 8000:
        money1 = money1 + 1
    elif data[11] < 3000:
        money2 = money2 + 1
    if data[5] .startswith('14' or '17'):
        phone1 = phone1 + 1
    elif data[5].startswith('13'):
        phone2 = phone2 + 1
    elif data[5].startswith('15'):
        phone3 = phone3 + 1
    if data[9] .startswith('黑龙江'):
        heilongjiang = heilongjiang + 1
    elif data[9].startswith('北京'):
        beijin = beijin + 1
    elif data[9].startswith('福建'):
        fujian = fujian + 1
    elif data[9].startswith('四川'):
        sichuan = sichuan + 1
    if data[13] .endswith('传媒有限公司'):
        gongsi = gongsi + 1
print("男生人数：",nan)
print('女生人数：',nv)
print('45岁以上的人数：',nianling)
print('工资8000以上的人数：',money1)
print('工资3000以下的人数：',money2)
print('电信人数：',phone1)
print('移动人数：',phone2)
print('联通人数：',phone3)
print("黑龙江",heilongjiang)
print('北京',beijin)
print('福建',fujian)
print('四川',sichuan)
print('传媒有限公司',gongsi)