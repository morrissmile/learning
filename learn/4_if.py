# x=int(input("請輸入數字   "))  #基本輸入是字串
# if x > 200:
#     print("over 200")
# elif x > 100:
#     print('over 100 below 200')
# else:
#     print('below 100')


#判斷式
if True:
    print("執行")
if False:   # 這個不會被執行 因為條件失敗
    print("執行")

#字串判斷
x ="rrr"
if x == 'rrr':
    print("rrr correct")
else:
    print("no~~")


#四則運算
s=[]
for i in range(2):
    data =int(input("請輸入1個數字   "))
    s= s+[data]

print(s)
logic=input("+,-,*,/   ")
if logic == '+':
    print(s[0]+s[1])
elif logic == '-':
    print(s[0]+s[1])
elif logic == '*':
    print(s[0]*s[1])
elif logic == '/':
    print(s[0]/s[1])
else:
    print('input error')

#python 不支援switch
#若要兩數直接交換可以用以下寫法1

# a=1
# b=2
# a, b=b, a
# print(a, b)
