#實體物件的建立與使用 - 上篇 - 實體屬性 Instance Attributes
#https://www.youtube.com/watch?v=Lr5N2r1rmtM&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=17
#類別的另一種用法

#類別有兩種的使用方式
# 1.類別與類別屬性  (=14 那篇的用法)
# 2.類別與實體物件 實體屬性

#實體物件
# 透過類別建立
# # 先定義類別 再透過類別建立實體物件
# #
# # 建立 > 使用
# # 要先建立實體物件 才能使用實體屬性

# class 類別名稱:
#     #定義初始化函式
#     def __init__(self):
#         透過操作self來定義實體屬性
#
# #建立實體物件 放入變數obj中
# obj =類別名稱() #呼叫初始化函式


# 程式範例
# class Ponit:
#     def __init__(self):
#         self.x=3
#         self.y=4
# #建立實體物件
# #此實體物件包含X和Y兩個實體屬性
# p=Ponit()


# 程式範例
# class Ponit:
#     def __init__(self, x, y):
#         self.x=x
#         self.y=y
# #建立實體物件
# #建立時 可直接傳入參數資料
# p=Ponit(1, 5)

#使用實體物件
# 基本語法
# 實體物件.實體屬性名稱
# 承上題
# 程式範例
# class Ponit:
#     def __init__(self, x, y):
#         self.x=x
#         self.y=y
# #建立實體物件
# #建立時 可直接傳入參數資料
# p=Ponit(1, 5)
# print("使用實體物件", p.x+p.y)


#point 實體物件的設計 :平面座標的點
class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y
p1 = Point(3, 4)
print("實體物件的設計 :平面座標的點p1", p1.x)
p2 = Point(5, 6)
print("實體物件的設計 :平面座標的點p2", p2.x, p2.y)
#利用這種寫法 可以建立很多實體物件


#範例2
#Fullname 實體物件的設計: 分開紀錄姓、名資跳的全名
class Fullname:
    def __init__(self, first, last):
        self.first = first
        self.last = last
name1 = Fullname("C.W", "Peng")
name2 = Fullname("Lin", "Ding")
print(name1.first, name1.last)
print(name2.first)

