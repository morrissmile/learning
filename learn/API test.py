import requests
import json

class Login():
    def __init__(self, email, password):
        self.LTURL = 'https://app.legaltemplates.net/api/v1'
        self.email = str(email)
        self.password = str(password)

    def userguest(self):
        url = self.LTURL + '/user/info'
        headers = {
            'Content-Type': 'application/json',
            }
        getapi = requests.get(url, headers=headers)
        print(url)
        print(getapi.json())
        # print(getapi.cookies)

        global guestcookie      #1
        guestcookie = getapi.cookies['_legaltemplates_session']  #2. 將區域變數變全域變數
        print(guestcookie)





    def signinapi(self):
        url = self.LTURL + '/users/sign_in'
        body = {"user": {"email": self.email, "password": self.password}}

        headers = {
            'Content-Type': 'application/json',
                   }

        postsignapi = requests.post(url, headers=headers, json=body)
        print(url)
        apicookie = postsignapi.cookies #將 cookie 存入變數
        print(type(apicookie))
        print(apicookie)  # 印出全部 cookie
        print(apicookie["_legaltemplates_session"])  #印出 cookie  _legaltemplates_session的值
        print(apicookie.keys()) #印出cookies 所有keys值 list格式輸出

        global user_legaltemplates_session   #  1.
        user_legaltemplates_session = apicookie["_legaltemplates_session"] #2. 將區域變數變全域變數


        result = postsignapi.json()  # 將 response 存入變數
        print(postsignapi.status_code)
        print('response', result)   # 印出全部 reponse
        print(result["email"]) #抓特定欄位的 值 因為整個是dic 輸入key值可以拿到value


    def verify_cookie(self):

        if guestcookie == user_legaltemplates_session:
            print('cookie _legaltemplates_session pass')
        else:
            print('cookie _legaltemplates_session fail')





account1 = Login('morris.lin+pro7@taroko.io', 'a12345678')
account1.userguest()
account1.signinapi()
account1.verify_cookie()
