# 建立與刪除
#
# dict={}: 建立空的dict
# del dict[key]: 刪除特定的key-value pari
# 增加與更新
#
# dict[key]=value: 如果key不存在，會增加這組K-V；如果key已存在，會更新這組K-V。
# for … in
#
# for [變數名稱] in dict:每一回合會拿到一把在dict裡的key，就可以用dict[key]拿到對應的變數。


# ● 小練習
#
# 讓使用者在名為table的dict中，輸入五組的key-value pair，key是字串、value是數字，最後把這個dict印出來。(提示: dict沒有append，直接用增加或更新(InsertOrUpdate)的方式)
table = {}
for i in range(0, 5):
    keya = str(input('key=' ))
    valuea = int(input('value=' ))
    table[keya]=valuea
print(table)


