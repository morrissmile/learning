import traceback
# if-else主要用在邏輯運算的判斷上：
#
# > 大於
# < 小於
# >= 大於等於
# <= 小於等於
# == 等於
# !== 不等於
# 或是布林值(Boolean)：
#
# true 真的
# false 假的
# and 且
# or 或
# not 非


#第一步讓使用者輸入想要做的符號運算，比如「+, -, *, /」，第二步讓使用者輸入’整數1’和 ‘整數2’，最後讓這兩個整數進行運算。如果輸入的運算符號不是「+, -, *, /」，便輸出「錯誤」。

x=input()
y=input()
z=input()


try:
    a=int(y)
    b=int(z)
    if x == '+':
        print('+', a + b)
    elif x == '-':
        print('-', a - b)
    elif x == '*':
        print('*', a * b)
    elif x == '/':
        print('/', a / b)
    else:
        print('error should input+-*/')

except ValueError:
    print('error please input int')
