#主程式
import geometry.point   #載入封包中的模組
result = geometry.point.distance(3,4)   #使用封包模組中的函式
print(result)

import geometry.line
lineresult = geometry.line.slope(1,1,3,3)
print("斜率", lineresult)
#封包可以很多層 但import就要相應的變動 所以可以用別名取代
#ex
import geometry.line as line
re = line.slope(1,1,3,3)
print(re)