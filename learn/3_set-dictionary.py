# 集合
# 可以用in or  not in還判斷有沒有值在裡面
# 交集聯集
# 使用&和|運算符號
# 差集 反交集
# 使用 - 和^運算符號
# 字串拆解為集合
# set(字串)
#
# 字典
# Key-value pair
# 字典[Key]
# 字典[Key]=value
# 可以用in or  not in還判斷有沒有值在裡面
# 可以用del刪除配對
# 可以以列表的資料為基礎建立字典



#集合的運算
s1={3,4,5}
print(3 in s1)  #確認 3是不是存在集合內
s2={4,5,6,7}
s3=s1&s2  #交集 取兩個集合中 相同的資料
print(s3)
s4=s1|s2 #聯集 取兩個集合中所有資料 但不重複
print(s4)
s5=s1-s2 #差集 從S1中減去S2重疊的部分 順序有差
print(s5)
s6=s1^s2 #反交集 取兩個集合中 不重複的部分
print(s6)
s=set("hello") #set(字串)  #會自動拆解字串進去集合 但不重複也沒順序性
print(s)
print("h" in s) #確認 h有沒有在這字串裡面

print("======字典=======")
#字典的運算
dic={"apple":"蘋果","banana":10} #一樣用大括號 但是要 key-value 的配對
print(dic["apple"],dic["banana"])
dic["apple"]="small apple" #更換value
print(dic["apple"])
print("apple" in dic)  #判斷key是否存在
print("test" in dic)
del dic["apple"] #刪除字典中的鍵值對(key-value pair)
print(dic)
dic.setdefault("c", 'qaq') #新增至dic內 但如果key值已經有 不會新增
print(dic)
#test={x:x*2 for x in [列表list]}  #for in是固定的 !!從列表的資料產生字典
test={x:x*2 for x in [3,4,5]}
print(test)

