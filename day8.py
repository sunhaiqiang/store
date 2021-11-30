"""
分析一个水杯，属性和行为，使用类描述并创建对象
属性：高度，容积，颜色，材质
行为：能存放液体

笔记本电脑
属性：屏幕大小，价格，cpu型号，内存大小，待机时长
行为：打字，打游戏，看视频

先构思面向对象版的中国工商银行系统

"""


# 水杯
class Cup:
    height = ""
    volume = ""
    colour = ""
    texture = ""

    def stockpile(self):
        print("一个高", self.height, "的", self.colour, self.texture, "里有", self.volume, "的水")


# 定义水杯
C = Cup()
C.height = "15公分"
C.volume = "250毫升"
C.colour = "白色"
C.texture = "陶瓷"
C.stockpile()


# 笔记本电脑
class Laptop:
    size = ""
    price = ""
    cpu_type = ""
    memory_size = ""
    standby_often = ""

    def type(self):
        print("我用着一个价格", self.price, self.standby_often, "的电脑在打字")

    def play_game(self):
        print("我用着一个价格", self.price, "显卡是", self.cpu_type, self.standby_often, "的电脑在打游戏")

    def watch_video(self):
        print("我用着一个价格", self.price, "显卡是", self.cpu_type, "内存是", self.memory_size, self.standby_often, "的电脑在看视频")


# 定义笔记本电脑
L = Laptop()
L.size = "15.6英寸"
L.price = "6300"
L.cpu_type = "i5-9300"
L.memory_size = "1T"
L.standby_often = "30小时"
L.type()
L.play_game()
L.watch_video()







