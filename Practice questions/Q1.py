#找出三位數的數字和為 10 且數字都不同的所有三位數， 例如：325、910，驗證共有 40 個數。

def findnum():
    ans = []
    for x in range(1, 10):
        for y in range(10):
            for z in range(10):
                if x+y+z == 10 and x != y and y != z and x != z:
                    num = str(x)+str(y)+str(z)
                    ans.append(num)

    print(ans)
    print(f"total have {len(ans)} numbers")


findnum()