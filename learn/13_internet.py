#Python 網路連線程式、公開資料串接
#https://www.youtube.com/watch?v=sUzR3QVBKIo&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=15

#網路連線
#載入模組
#import urllib.request

#下載特定網址資料
# import urllib.request as request
# with request.urlopen(網址) as response:
#     data=response.read()
# print(data)

#公開資料
#適合的資料來源 => 台北市政府公開資料
#確認資料格式   JSON CSV or 其他格式
#解讀JSON 格式  使用內建的josn模組


#範例
#網路連線
# import urllib.request as request
# src = "https://www.google.com"
# with request.urlopen(src) as response:
#     data = response.read().decode("utf-8")  #取得網站的原始碼(HTML CSS JS) 有中文字要加decode
# print(data)


#https://data.taipei/#/dataset/detail?id=15c3e1ae-899b-466c-a536-208497e3a369  台北市政府 內湖科技廠商 API 網頁位置
#API  https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire
import urllib.request as request
import json  #因為API內容是JSON格式
src = "https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
with request.urlopen(src) as response:
    data = json.load(response)
#print(data) #印出API內容的
#用法 例如 將公司名稱列表出來 不然一整塊資料沒用
companylist = data["result"]["results"]  #這格式來自於josn檔 整份放在data內 我們要data內的 result底下的results內容   #先拿到列表
# print(companylist)
# for company in companylist:
#     print(company["公司名稱"])  #他是一個字典 所以用key值印出 value
# 若要寫成檔案
with open('lesson13.txt', mode='w', encoding='utf-8') as lesson13file:
    for company in companylist:
        lesson13file.write(company['公司名稱']+'\n')  #寫入檔案 並且每一筆換行
    