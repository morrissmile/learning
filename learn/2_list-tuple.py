#有序可變動列表 List
grades=[12,60,15,70,90]
list2=[11,22,33]
print(grades)
print(grades[0])    #只抓列表第一個資料
print(grades[1:4])  #只抓第一個開始 第四個以前的資料
grades[0]= 100  #更新列表0的值
print(grades)
grades[1:4]=[]  #把從1開始到第四個以前資料刪除
print(grades)
grades[1:4]=[300,400,500] #把從1開始到第四個以前資料更換 會移除第四個資料
print(grades)
grades=grades+[12,33] #增加12,33到列表裡面
print(grades)
print(len(grades)) #取列表長度
grades.insert(1,999)  #第一位插入999數值
print(grades)
grades=grades+list2 #兩個list合併並存回list1裡面
print(grades)

#刪除方法
del grades[2] #刪除位置2的值
print(grades)

grades.pop()  #刪除最後一個元素
grades.remove(11) #刪除特定的值
print(grades)

#巢狀列表
print("巢狀")
data=[[3,4,5],[6,7,8]]
print(data[0][0])   #抓第一個列表第一個值
data[0][0:2]=[5,5,5]  #從第0個到第2個以前換成 5 5 5 ,原本還有最後一個5 所以便4個5
print(data)
data.append(1)  #這也是增加數值到陣列的方式
print(data)

#有序不可動列表 Tuple
tupl=(3,4,5)
# data[0]=5 #會錯誤 因為不可更變數值
tupl=tupl+(1,2) #增加值進去列表裡面
print(tupl)
del tupl #刪除tupl資料 無法只刪除單獨幾個數字 只能全部移除
print(tupl)