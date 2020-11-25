#實體物件的建立與使用 - 下篇 - 實體方法 -
#https://www.youtube.com/watch?v=MZtTClJ74NU&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=18

#class 類別名稱:
#定義初始化函式
#     def __init__(self):
#          定義實體屬性
#     # 定義實體方法/函式
#       def 方法名稱(self, 更多自訂參數) :
#           方法主體 透過self 操作實體物件
#     #建立實體物件 放入變數obj中
# obj=類別名稱()

#使用方法
# 實體物件.實體方法名稱(參數資料)  #有需要參數資料才要寫參數資料
#範例
class Ponit:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def show(self):
        print(self.x, self.y)
    def show2(self, h, z):
        print(h, z)
p=Ponit(1, 5) #建立實體物件
p.show() #呼叫實體方法 利用實體資料
p.show2(88, 99) #直接帶數值給def寫法



#
#PP 實體物件的設計 平面上的點
class PPP:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    #定義實體方法
    def show(self):
        print(self.x, self.y)
    def distance(self, targetx, targety):
        return ((self.x - targetx)**2+(self.y - targety)**2)**0.5 #計算兩點距離公式

pp = PPP(3, 4)
pp.show()
result=pp.distance(0, 0)
print("計算兩點距離公式  ", result)


# File 實體物件的設計 : 包裝檔案讀取的程式
class Flie:
    def __init__(self, name):
        self.name = name
        self.file = None  # 尚未開啟檔案 初期是none

    def loadfile(self):
        with open(self.name, mode="r" ,encoding="utf-8") as files:
            self.file = files
            return self.file.read()

f1 = Flie("lesson13.txt")
data = f1.loadfile()
print("f1 file open: ", data)
