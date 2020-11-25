#break 強制結束迴圈
q=0
while q<5:
    if q==3:
        break
    q+=1
    print('break test:  ', q)

#continue 強制進入下一圈

#ex:
n=0
for x in [0,1,2,3]:
    if x%2==0: # %=取餘數
        continue
    n+=1
print('continue tesk:  ', n)  #原本要跑4次 因為兩次可以整除 所以跳過兩次


# #else
# while 布林值:
#     若布林值為True 執行命令
# else:
#     迴圈結束前 執行此區塊命令 (上面都跑完了 會執行這區一次)
#
# for
#  .....
# else
#  .....  用法同上

n=1
while n < 5:
    print(n)
    n+=1
else:
    print('loop finish')

print("=============================")


#practice
#綜合範例 : 找出整數平方根
#輸入9,得到3
#輸入11,得到沒有整數的平方根
#寫法1
# y = int(input("input 1 int num:  "))
# test= y**0.5
# if isinstance(test, int) == True:
#     print(test)
# else:
#     print('沒有整數平方根')

bb=int(input("input 1 int num   "))
for qqq in range(bb): #qqq 從 0~n-1
    if qqq*qqq==bb:
        print("平方根",qqq)
        break #用 break 結束迴圈 不會執行else
else:
    print("沒有整數平方根")






