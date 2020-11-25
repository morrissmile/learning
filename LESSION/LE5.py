# #現在有一個 list a = [1, 3, 5, 7, 9]，請對每一個元素都平方後印出來，且須將 a 也變成 [1, 9, 25, 49, 81]。
q = [1, 3, 5, 7, 9]
for i in range(len(q)):
    print(q[i]*q[i], end=' ')
    print(end='\n')
    q[i]=q[i]*q[i]
print(q)
#
# #建立一個空的list: a = list() 或是 a = []都可以
# # 動態增加元素:
# # #
# # # list.append(x): 把變數x塞到list的最後面
# # # list.insert(i, x): 把變數x塞到i這個位置上
# # # list.pop(): 把list的最後一格丟掉
# # # list.pop(i): 把list的第i格丟掉
# # # list.remove(x): 會把第一個出現的變數x拿掉
# # # list.clear(): 把list內的資料全部清光光
# # # 與常見函數的結合:
# # #
# # # max(list): 找出list中最大值
# # # min(list): 找出list中最小值
# # # sum(list): 找出list數字總和
print('===================')

a = [10, 30, 50, 70, 90]
b=[]
avg=sum(a)/len(a)
print('avg=', avg)
for w in range(len(a)):
    c=(a[w] ** 0.5)*10
    b.append(c)
print(b)

newavg=sum(b)/len(b)
print('newavg=', newavg)

# 針對slice語法，讓我們深入介紹一些細節部分：
#
# list[start: end]，start和end都可以省略不寫
# start的預設為0
# end的預設為len(list)
# liest[ :end]代表 0~end-1
# list[start: ]代表start~len(list)-1
# list[ : ]代表0~len(list)-1

# h = ['r', 'rr', 'rrr', 'rrrr', 'g', 'gg', 'ggg']
# # print(h[2:4])
# # print(h[1:4])
# # print(h[0:4])

#輸入十個整數、存入一個名為people清單中 (表示我們的宴客人數)；之後會有五次詢問，每次會輸入清單開始和結束的位置，再輸出從開始到結束位置的總和。
print('please input people data')
people = []
for o in range(5):
    people.append(int(input()))
print(people)

for p in range(5):
    print('input start data')
    start = int(input())
    print('input end data')
    end = int(input())
    print(sum(people[start:end]))
