# def 函式名稱(參數名稱=預設資料):
#     函式內部的程式碼
#參數可給預設值 但必須放在一般參數之後
def say(msg="hello"):
    print(msg)
say("hihi")
say()  #會印出預設資料 hello

#名稱對應
# def 函式名稱(名稱1, 名稱2):
#     函式內部的程式碼
# #呼叫函式 以參數名稱對應資料
# 函式名稱(名稱2=3, 名稱1=5) 若不指定 要造順序給
def divide(n1, n2):
    result=n1/n2
    print("divide:  ", result)
divide(2, 4)
divide(n2=2, n1=4)

#無限參數
# def 函式名稱(*無限參數)   #參數名稱前面+ "*"等於無限參數
#     無限參數以Tuple資料形態處理
#     函式內部的程式碼
# #呼叫函式，可傳入無線數量的參數
# 函式名稱(資料1, 資料2, 資料3)

#範例
#函式接受無限參數msgs
def saylimit(*msgs):
    #以Tuple的方式處理
    for msgg in msgs:
        print(msgg)
saylimit("hi", "hihi", "hihihi")



print("=====實際程式撰寫======")
#實際程式撰寫
#參數的預設資料 和參數的名稱對應
def power(base, exp=0):
    print(base**exp)
power(3,2)
power(exp=3, base=2) #參數的名稱對應
power(4)  #預設為0 所以4的0次方為1

#無限/不定量 參數資料
#做總量平均數 但數字量不固定  avg(3,4) avg(3,5,10) avg(1,4,-1,-8)
print("做總量平均數 但數字量不固定  avg(3,4) avg(3,5,10) avg(1,4,-1,-8)")
def avg(*num):
    sum = 0
    avgs = 0
    for i in num:
        sum = sum + i
    avgs = sum / len(num)
    print(avgs)

avg(3, 4)
avg(3, 5, 10)
avg(1 ,4, -1, -8)

#另外寫法
# def avg(*num):
#     sum = 0
#     for i in num:
#         sum = sum + i
#     print(sum / len(num))
#
# avg(3, 4)
# avg(3, 5, 10)
# avg(1 ,4, -1, -8)
