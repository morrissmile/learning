# 那如果有了key，想要把dict中相對應的資料取出來應該要怎麼做呢? 作法有兩個：
#
# d[key]: 這個做法相對不安全，key如果不存在的話就會出現KeyError (如同上面我們所示範的)。
# d.get(key, default_value): 是比較安全的作法，如果key不存在的話就會回傳 default_value (下面例子中的deafult_value就是’找不到耶’)。

# ● 小練習
#
# 一年一度的世界歌王大賽來啦！身為評審的你，請輸入三個歌手的名字與成績。接下來會有三次查詢的機會，每次查詢都可以讓觀眾輸入一個名字、來查看心愛的歌手。
#
# 如果歌手不在名單中，請輸出’這個人沒參賽喲’；如果歌手在名單中，請輸出該歌手的名字與成績。
singlist = {}
for i in range(0, 3):
    name = input('singername=' )
    value = input('value=' )
    singlist[name] = value

for j in range(0, 3):
    search = input('input_singername=' )
    print(singlist.get(search, 'Can\'t find'))


