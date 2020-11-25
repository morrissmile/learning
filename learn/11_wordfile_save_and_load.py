#基本語法
# 檔案物件=open(檔案路徑,mode=開啟模式)
#
# 開啟模式
# 讀取模式 -r
# 寫入模式 -w
# 讀寫模式 -r+
#
# 讀取檔案
# 讀取全部文字
# 檔案物件.read
#
# 一次讀取一行
# for 變數 in 檔案物件
#     從檔案依序讀取每行文字到變數中
#
# 讀取JSON格式
# import json
# 讀取到的資料=json.load(檔案物件)
#
# 寫入(儲存)檔案
# 檔案物件.write(字串)
#
# 寫入換行符號
# 檔案檔案物件.write("這是範例文字\n")  #\n是換行符號
#
# 寫入JSON格式
# import json
# json.dump(要寫入的資料, 檔案物件)
#
# 關閉檔案
# 檔案物件.close()


# #最佳實務的語法
# with open(檔案路徑, mode=開始模式) as 檔案物件(檔案別名也行):        #63行有範例
#     讀取或寫入檔案的程式
# #這個寫法 區塊會自動 安全的關閉檔案

#======================================================
#範例
#儲存檔案
# file = open("data.txt", mode="w") #開啟寫入模式
# file.write("hihi\n hihi(secline)") #操作
# file.close()  #關閉
#
# #若要用中文
# filech = open("datach.txt", mode="w", encoding="utf-8") #開啟寫入模式 #若有中文 要加上編碼
# filech.write("hihi\n 你好 ") #操作
# filech.close()  #關閉
#
# #最佳實務的寫法
# with open("data1.txt", mode="w") as file:
#     file.write("test")
#
#
# #===============================================================
# #讀取檔案
# with open("data.txt", mode="r") as file:
#     dataload=file.read()
# print(dataload)

# #若檔案是多行數字 並且每一行數字作加法
# sum=0
# with open("datatest.txt", mode="w") as testfile:
#     testfile.write("5\n3\n4")   #建立檔案
# with open("datatest.txt", mode="r") as testfile:
#     for line in testfile:  #一行一行去讀取
#         sum=sum+int(line)
#     print(sum)

#使用Json格式讀取 複寫檔案
# import json
# with open("config.json", mode="r") as jsonfile:
#     jsontest=json.load(jsonfile)
# print(jsontest) #jsontest 是一個字典資料
# # print("name: ", jsontest["name"])  #只印出name的 value
# # print("version: ", jsontest["version"])
# jsontest["name"]="new name" #修改變數資料
# #把最新的資料複寫回檔案
# with open("config.json", mode="w") as jsonfile:
#     json.dump(jsontest, jsonfile)  #會將name 從 my name改成new name



# 檔案內容有3行 qq qq2 qq3 將qq更換成RR
#建立檔案並確認內容正確
with open("testwordfile", mode="w") as test:
    test.write("qq\nqq2\nqq3")
with open("testwordfile", mode="r") as test:
    content = test.read()
print(content)

#將內容讀取出來並修改存回
a=[]
contentqwe=""
with open("testwordfile", mode="r") as test:
    for qwe in test:
        contentqwe = qwe.replace("\n",'') #將換行符號移除 不然list內容會是['qq\n', 'qq2\n', 'qq3']
        print(contentqwe)
        if contentqwe == "qq":
            contentqwe = "RR"
            a.append(contentqwe)
        else:
            a.append(contentqwe)
print(a)
with open("testwordfile", mode="w") as test:
    for tx in a:
        test.write(tx+'\n')
