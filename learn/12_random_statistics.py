#亂數和統計模組
#https://www.youtube.com/watch?v=-xwCu6PN1jU&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=14
import random
#從列表中隨機選一個資料
random.choice([0,1,5,8])

##從列表中隨機選兩個資料
random.sample([0,1,5,8],2)

##從列表中隨機選3個資料
a = random.sample([0,1,5,8],3)
print(a)

#隨機調換順序
#將列表中的資料[就地]隨機對調順序
data=[0, 1, 5, 8]
random.shuffle(data)
print('隨機調換順序  ', data)

#隨機取得亂數
random.random()
random.uniform(0.0, 1.0) #取得0.0~1.0之間的隨機亂數

#常態分配亂數
#取得平均數 100 標準差10的 常態分配亂數  (等於大部分抓 90~110 的數字)
random.normalvariate(100, 10)

#======================================
#統計模組
# import statistics #載入模組
# #計算列表中數字的平均數
# statistics.mean([1, 4, 6, 9])
# #計算標準差
# statistics.stdev([1, 4, 6, 9])  #計算列表中數字的標準差



#"================================================="
#範例
#隨機模組
import random
#隨機選取
d = random.choice([1, 5, 6, 9, 10, 20])
print("隨機選取:   ", d)
#隨機選取任意筆資料
e = random.sample([1, 5, 6, 9, 10, 20], 4)
print("隨機選取:   ", e)

#隨機取得亂數
da = random.random()    #預設值為0~1之間的亂數 會有小數點
print("random.random:", da)
#也可以寫成
da2 = random.uniform(10.0, 100.0)  #10~100之間
print(da2)

dint = random.randint(0, 100)  #10~100之間的整數
print(dint)
#或是
da3 = int(random.uniform(10.0, 100.0))  #10~100之間
print("da3", da3)


#統計模組
import  statistics as stat
stdata= stat.mean([1, 2, 3, 4, 5, 8, 100]) #mean=計算平均數
print("平均數: ", stdata)
stmiddata= stat.median([1, 2, 3, 4, 5, 8, 100]) #median 計算中位數
print("中位數: ", stmiddata)

stdevdata= stat.stdev([1, 2, 3, 4, 5, 8, 100])  #計算標準差
print("標準差: ", stdevdata)



print("練習題")
#練習題 隨機產生n個0~10的數 但不會重複 至少產生兩個數字
def randomnum(sta, end, n=2):
    numberlist = []
    m = 0
    while m < n:
        randomnumber = int(random.uniform(sta, end))

        if randomnumber not in numberlist:
            numberlist.append(randomnumber)
            m = m + 1


    print(f"練習題 random {n} numbers from {sta} to {end}, {numberlist}")

randomnum(0, 10)
randomnum(0, 10, 8)
randomnum(0, 100, 10)

print("練習題另種寫法")
#練習題 隨機產生n個0~10的數 但不會重複 至少產生兩個數字
def randomnum1(sta, end, n=2):
    numlist = []
    for i in range(sta, end+1):
        numlist.append(i)
    resultnumlist = random.sample(numlist, n)

    print(f"練習題 random {n} numbers from {sta} to {end}, {resultnumlist}")

randomnum(0, 10)
randomnum(0, 10, 8)
randomnum(0, 100, 10)
