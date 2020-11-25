# import sys
# sys.path.append("modules")
# import loadfile  #因為將modules放在資料夾內 所以要先增加modules 到sys路徑裡面 才能import

# 或寫這樣  from package import module
from modules import loadfile


if __name__ == '__main__':
    f2 = loadfile.Flie('lesson13.txt')
    data = f2.loadfile()
    print('f2', data)



# 或寫這樣
import modules.loadfile

if __name__ == '__main__':
    f3 = modules.loadfile.Flie('lesson13.txt')
    data = f3.loadfile()
    print('f3', data)