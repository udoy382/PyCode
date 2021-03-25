# Request Module For HTTP Requests #81


import requests

#       make a get request variable then set url this urls comes from [ https://financialmodelingprep.com ] this website.
r = requests.get("https://financialmodelingprep.com/api/v3/profile/AAPL?apikey=demo")
print(r.text)

#       this is print stastment shows owr status code [ search on google status code ].
print(r.status_code)

#       this method use for print request post.
# url = "www.something.com"
# data = {
#     "p1":4,
#     "pt":8
# }

# r2 = requests.post(url=url, data=data)

# ---------------------------------------------------
# Others... requests function
# ----------------------------------------------------

#       this is first functon to print payload.
# payload = {'key1':'value1'}
# res = requests.get('https://httpbin.org/get', params=payload)
# print(res.url)

#       this is second function to print post request.
# payload = {'key1':'value1'}
# res = requests.post('https://httpbin.org/post', data=payload)
# print(res.text)

#       and others function...
# cookies = dict(key1='value1')
# res = requests.get('https://httpbin.org/headers')

# print(res.status_code)
# print(res.cookies)
# print(res.headers)
# print(res.json())
# print(res.headers)