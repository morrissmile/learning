# 1. 利用List資料組的append()方法
# append()方法一次只能夠加入一項資料，而且是加在資料組的最後面。
#
# x.append(300)
# x.append('Tom')
# x.append([50, 60])   # [50, 60]會當成一筆資料加入
#
# 2. 利用List資料組的extend()方法
# extend()方法可以一次把多項資料加在原來資料的最後，但是必須把這些資料放在一個List資料組，或是Tuple資料組裏頭。
#
# x.extend([300])   # 把要加入的資料放在資料組裏頭
# x.extend([50, 60])   # 50和60會當成二筆資料加入

#輸入十個整數、存入一個名為people清單中 (表示我們的宴客人數)；之後會有五次詢問，每次會輸入清單開始和結束的位置，再輸出從開始到結束位置的總和。
people = []
que = []
for i in range(0, 5):
    peo =int(input('input number:'))
    people.append(peo)
print(people)

for j in range(0, 2):
    a = int(input('start:'))
    b = int(input('end:'))
    que.extend(people[a:b])
print(que)
print(sum(que))