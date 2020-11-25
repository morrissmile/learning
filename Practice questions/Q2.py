import requests
import json

r = requests.get('https://www.google.com.tw')
print(r.status_code)



headers = {
    "Cookie" : "sails.sid=s%3AiS6B155bNxqeUSwdON4FZK_7pUxGmZFI.gndK5AeaEwNft39nHP3lrCX5nl2FWmRU7gg%2Bc2eb5lc",
    "Postman-Token" : "<calculated when request is sent>",
    "Content-Length" : '0',
    "User-Agent" : "PostmanRuntime/7.26.5",
    "Content-Type" : "text/plain"
}

body = {
    'foo1' : 123,
    'foo2' : 'abc'
}

post = requests.post('https://postman-echo.com/post', headers=headers, json=body)
print(post.status_code)
result = post.json()
print(result)

#
# post(url, data=None, json=None, **kwargs)
#     Sends a POST request.
#
#     :param url: URL for the new :class:`Request` object.
#     :param data: (optional) Dictionary, bytes, or file-like object to send in the body of the :class:`Request`.
#     :param json: (optional) json data to send in the body of the :class:`Request`.
#     :param \*\*kwargs: Optional arguments that ``request`` takes.
#     :return: :class:`Response <Response>` object
#     :rtype: requests.Response
#
# So data can be a dictionary, string/bytes, or a file-like object.
#
# Perhaps you need to specify the Content-Type header like this:
#
# requests.post(url, data=raw_data, headers={'Content-Type': 'application/x-www-form-urlencoded'})

