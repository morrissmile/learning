#獨立的程式檔案
#將程式寫在一個檔案中，此檔案可重複載入使用
#載入>使用  先載入模組後在使用模組中的函式或變數

#載入模組方式
#import 模組名稱   #模組名稱=檔案名稱不用加副檔名
#import 模組名稱 as 模組別名


# 使用模組
# 模組名稱或別名.函數名稱(參數資料)
# 模組名稱或別名.變數名稱
#
# 內建模組
# #sys模組  取得系統相關資訊
# 範例
# import sys
# print(sys.platform) #印出作業系統
# print(sys.maxsize) #印出整數型態最大值
# print(sys.path) #印出收尋模組路徑

# 另一種用法
# import sys as s
# print(s.platform) #印出作業系統
# print(s.maxsize) #印出整數型態最大值
# print(s.path) #印出收尋模組路徑


#範例 建立幾何運算模組
# 建立檔案 geometry.py 定義平面幾何運算式用函數
# 請看 dic > excode


