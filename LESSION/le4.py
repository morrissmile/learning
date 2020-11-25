#for [變數名稱] in range(n): (縮排) print([變數名稱])

#99乘法
#print出來的結果換行且要有空格，可以使用end=’ ’；若要再換行可使用end=’\n’
#range 的結構是：range(起點, 終點, 間距)，其中的間距預設為1 、比如 range(0, 6) = range(0, 6, 1) 。代表從 0 到 5，每次加 1 的意思。
for i in range(1,10):
    for j in range(1,10):
        x=i*j
        print(x, end=' ')
    print(end='\n')

#猜數字的程式：每次讓使用者猜一個整數，若猜對就輸出Bingo；使用者最多可以猜3次。(提示: Bingo後可以使用break來離開迴圈)
ans=35

print('input a 10~100 number')

try:
    for i in range(3):
        m=int(input())

        if ans == m:
            print('bingo')
            break
        else:
            print('try again')
    print('game over')
except ValueError:
    print('please input int')