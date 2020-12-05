class digua:
    def __init__(self):
        self.time = 0
        self.zhuang = "生的"
        self.liao = []

    def kehu(self,add):
        self.time += add

        if 0 < self.time <= 3:
            self.zhuang = "生的"
        elif 3 < self.time <= 5:
            self.zhuang ="半生不熟"
        elif 5 < self.time <= 8:
            self.zhuang = "熟的"
        elif self.time > 8:
            self.zhuang = "熟透了"
        print(self.zhuang)
    def tiaoliao(self,tiao):
        print("这是您的调料：",tiao)


abc = digua()
abc.kehu(9)

tiao = input("添加您的调料")
abc.tiaoliao(tiao)



class FOO:
    def __call__(self, *args, **kwargs):
        print("1. __call__    //对象可以直接执行")
        print("obj()")
obj = FOO()
obj()

