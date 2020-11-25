# 類別的定義與使用 - Class Attributes

#程式分門別類的工具，package 是最上層，接著是 module，接著是 class。
#看實際的情況自己決定要怎麼用就可以嘍 ~

# https://www.youtube.com/watch?v=uPKgQ3FoVtY&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=16
# 封裝變數或函式
# 封裝的變數或函式 統稱為類別的屬性

#定義 > 使用
#要先定義(建立)類別 然後才能使用類別中封裝的屬性


#定義類別
# 基本語法
# class 類別名稱:
#     定義封裝的變數
#     定義封裝的函式

#範例
#定義test 類別
# class Test:
# #     x=3 #定義變數
# #     def say(self): #定義函式
# #         print("hello")
# #
# # 使用類別
# # 基本語法
# # 類別名稱.屬性名稱
# #
# # Test.x+3  #取得屬性X的資料3
# # Test.say()  #呼叫屬性say函式

#實際範例
#定義類別 與類別屬性(封裝在類別中的變數和函式)
#定義一個類別IO 有兩個屬性supportedSrcs 和 read
class IO:
    supportedSrcs=["console", "file"]
    def read(src):
        if src not in IO.supportedSrcs:
            print("not support")
        else:
            print("Read from", src)
#使用類別
print(IO.supportedSrcs)
IO.read("file")
IO.read("fileqqqqq")




# 我們可以把 class 的定義放在模組中，然後引入模組來使用 class。
#
# 例如模組 mod.py：
# y=4;
# class Test:
#     x=3
#
# 加上主程式 main.py：
# import mod
# print(mod.y)
# print(mod.Test.x)