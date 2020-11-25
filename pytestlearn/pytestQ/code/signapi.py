import requests
import json

class Login():
    def __init__(self, email, password):
        self.LTURL = 'https://app.legaltemplates.net/api/v1'
        self.email = str(email)
        self.password = str(password)

    def signinapi(self):
        url = self.LTURL + '/users/sign_in'
        body = {"user": {"email": self.email, "password": self.password}}

        headers = {
            'Content-Type': 'application/json',
                   }

        postsignapi = requests.post(url, headers=headers, json=body)
        apicookie = postsignapi.cookies #將 cookie 存入變數


        global user_legaltemplates_session   #  1.
        user_legaltemplates_session = apicookie["_legaltemplates_session"] #2. 將區域變數變全域變數


        result = postsignapi.json()  # 將 response 存入變數
        return result["email"]


