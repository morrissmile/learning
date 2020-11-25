# File 實體物件的設計 : 包裝檔案讀取的程式
class Flie:
    def __init__(self, name):
        self.name = name
        self.file = None  # 尚未開啟檔案 初期是none

    def loadfile(self):
        with open(self.name, mode="r" ,encoding="utf-8") as files:
            self.file = files
            return self.file.read()

if __name__ == '__main__':
    f1 = Flie("lesson13.txt")
    data = f1.loadfile()
    print("f1 file open: ", data)
