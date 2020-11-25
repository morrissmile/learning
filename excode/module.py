#建立內建的sys模組並取得資訊
import sys
print(sys.platform)

import sys as system
print(system.maxsize)

print("======================")
#建立geometry模組 載入使用
#
# import geometry  #這是模組跟主程式同一層 或是以下的順序收尋找的到的位置
# dis = geometry.distance(1,1,5,5)
# print(dis)
# slope1 = geometry.slope(1,2,5,6)
# print("斜率:", slope1)

#調整收尋模組的路徑
import sys
print(sys.path)#印出模組的收尋路徑
#按照順序去收尋模組

#若將模組放到modules資料夾 會找不到  因為收尋路徑沒有modules資料夾  所以import指令要改
import sys
sys.path.append("modules")  #可以寫絕對路徑或相對路徑  #在模組的收尋路徑列表中[新增路徑]
import geometry
dis = geometry.distance(1,1,5,5)
print(dis)
slope1 = geometry.slope(1,2,5,6)
print("斜率:", slope1)

print(sys.path) #可以再路徑中找到modules 以後找模組也會找剛剛新增的資料夾
