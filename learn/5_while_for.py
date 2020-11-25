# # while m....
# while 判斷式:
# ex
# n=0
# while n<5:
#     print(n)
#     n+=1
# 可以印出0~4

#for...
# for 變數名稱 in 列表或字串:
#     將列表或字串的字元一一取出處理
#ex......:
for x in [4,1,2]:
    print("印出資料  ", x)
for c in 'hi':
    print('印出字串中的字元', c)
# #使用range()
# range(3)  = [0,1,2]
# for q in range(4) 相當於 for q in [0,1,2,3]
# # range(3,6) ==> [3,4,5]  開頭開始不包含結尾

# practice
# while
# while True: (無限迴圈)
# m從1+到10
m=1
sum=0
while m < 11:
    sum = sum + m
    m+=1
print('1+~10: ', sum)

#用for寫法
forsum=0
for s in range(11):
    forsum = forsum+s
print(forsum)