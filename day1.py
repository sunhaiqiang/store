print("日期       服装名称       价格/件       库存数量        销售量/每日")
print("1号        羽绒服        253.6         500              10  ")
print("2号        牛仔裤        86.3          600              60 ")
print("3号        风衣          96.8          335              43  ")
print("4号        皮草          135.9         855              63  ")
print("5号        T血          65.8          632               63  ")
print("6号        衬衫          49.3          562              120  ")
print("7号        牛仔裤        86.3          600               72  ")
print("8号        羽绒服        253.6         500               69  ")
print("9号        牛仔裤        86.3          600               35  ")
print("10号       羽绒服        253.6         500              140  ")
print("11号       牛仔裤        86.3          600               90  ")
print("12号       皮草         135.9         855               24  ")
print("13号       T血          65.8          632               45  ")
print("14号       风衣         96.8          335               25  ")
print("15号       牛仔裤        86.3         600               60  ")
print("16号       T血          65.8          632              129  ")
print("17号       羽绒服        253.6         500              10  ")
print("18号       风衣          96.8          335              43    ")
print("19号       T血          65.8          632              63  ")
print("20号       牛仔裤        86.3          600              60  ")
print("21号       皮草          135.9        135.9             63   ")
print("22号       风衣          96.8         96.8              60  ")
print("23号       T血           65.8         65.8             58  ")
print("24号       牛仔裤        86.3          600              140  ")
print("25号       T血           65.8         632              48  ")
print("26号       风衣          96.8          96.8             43  ")
print("27号       皮草          135.9         135.9            57  ")
print("28号       羽绒服        253.6          500              10  ")
print("29号       T血           65.8          632              63  ")
print("30号       风衣          96.8          335              78  ")
sales=253.6*10+253.6*69+253.6*140+253.6*10+253.6*10+86.3*60+96.8*43+135.9*63+65.8*63+49.3*120+86.3*72+86.3*35+86.3*90+135.9*24+65.8*45+96.8*25+86.3*60+65.8*129+96.8*43+65.8*63+86.3*60+135.9*63+96.8*60+65.8*58+86.3*140+65.8*48+96.8*43+135.9*57+65.8*63+96.8*78
sum = 10+60+43+63+63+120+72+96+35+140+90+24+45+25+60+129+10+43+63+60+63+60+58+140+48+43+57+10+63+78
downjacket=10+60+140+10+10
a = '{:.2%}'.format(downjacket/sum)
jeans=60+72+35+90+60+60+140
b = '{:.2%}'.format(jeans/sum)
dustcoat=43+2+43+60+43+78
c = '{:.2%}'.format(dustcoat/sum)
fur=63+24+63+57
d = '{:.2%}'.format(fur/sum)
Tshirt=63+45+129+63+58+48+63
e = '{:.2%}'.format(Tshirt/sum)
shirt=120
f = '{:.2%}'.format(shirt/sum)
average=sum/30
print("总销售额",sales)
print("平均每日销售量",average)
print("羽绒服的月销售量占比",a)
print("牛仔裤的月销售量占比",b)
print("风衣的月销售量占比",c)
print("皮草的月销售量占比",d)
print("T血的月销售量占比",e)
print("衬衫的月销售量占比",f)