#def 函式名稱(參數名稱):
#   程式碼

#範例
def say(msg):
    print('ex1:  ', msg)
say('hihihi')

#範例
def add(n1, n2):
    result=n1+n2
    print('ex2:  ', result)
add(22, 33)


#!!!!!回傳值!!!!!
#def 函式名稱(參數名稱):
    # 函式內部的程式碼
    # return  #結束函式,回傳None  最後一行沒寫return 也會自動return
#return 資料 #結束函數 回傳資料(字串 數字 列表 字典.....)

#範例
def say1(msg):
    print('回傳值範例1:  ', msg)
    return
say1('hihihi') #單純呼叫 所以會印出print那行 不會拿到回傳值
value = say1('hihihi')
print(value)   #會得到none 因為會拿到return的值


def add2(m1, m2):
    ans = m1+m2
    return ans
value1 = add2(55, 66)
print('範例add2:  ', value1)


#定義函式
#函式內部程式碼 沒有被呼叫就不會執行]
#參數可給預設值 但必須放在一般參數之後
def multiply(n1, n2, n3=1, n4=2):
    print(n1*n2)
    print(n3*n4)
multiply(3,5)
multiply(3,5,9,8)

#回傳值的好處是可以在外部繼續處理
#EX
def multiply1(n1, n2):
    return n1*n2
va = multiply1(3,4)+multiply1(5,6)
print('multiply1:  ', va)

#程式的包裝
# sum = 0
# for n in range(11):
#     sum=sum+n
# print(sum)
#舊有的寫法 1+~10 若要改成1+到20 就要再寫一次  但若改成函數
def calculate(qq):
    sum=0
    for n in range(qq):
        sum = sum + n
    qq -= 1
    print(f"1+~{qq}:   ", sum)
calculate(11)
calculate(21)







#呼叫函式