import requests,time,execjs
import json
from urllib.parse import urlencode

with open('X-APIKEY.js', 'r', encoding='utf-8') as f:
    js = f.read()
    ctx = execjs.compile(js).call('getApiKey')
pages = 5
for i in range(pages):
    page = i * 20
baseurl = 'https://www.oklink.com/api/explorer/v1/btc/transactionsNoRestrict'
data = {
    'offset':page,
    'limit':'20',
    'needBigField':'false',
    't':str(int(time.time()*1000))
}
url = f'{baseurl}?{urlencode(data)}'
headers = {
    "accept": "application/json",
    "accept-language": "zh-CN,zh;q=0.9",
    "app-type": "web",
    "devid": "2c50d584-e599-47f3-a55c-21698ecc0117",
    "priority": "u=1, i",
    "referer": "https://www.oklink.com/zh-hans/bitcoin/tx-list/page/3",
    "sec-ch-ua": "\"Chromium\";v=\"140\", \"Not=A?Brand\";v=\"24\", \"Microsoft Edge\";v=\"140\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0",
    "x-apikey": ctx,
    "x-cdn": "https://static.oklink.com",
    "x-id-group": "2940184243191380001-c-4",
    "x-locale": "zh_CN",
    "x-simulated-trading": "undefined",
    "x-site-info": "9FjOikHdpRnblJCLiskTJx0SPJiOiUGZvNmIsIiTDJiOi42bpdWZyJye",
    "x-utc": "8",
    "x-zkdex-env": "0"
}
cookies = {
    "aliyungf_tc": "f1695cfa4d23a8ec3e91d327a454533b40a44d4f320d2bdb2230435360676841",
    "devId": "2c50d584-e599-47f3-a55c-21698ecc0117",
    "ok_site_info": "9FjOikHdpRnblJCLiskTJx0SPJiOiUGZvNmIsIiTDJiOi42bpdWZyJye",
    "locale": "zh_CN",
    "ok-exp-time": "1758424290055",
    "fingerprint_id": "2c50d584-e599-47f3-a55c-21698ecc0117",
    "fp_s": "-1",
    "traceId": "2940184243191380001",
    "first_ref": "https%3A%2F%2Fwww.oklink.com%2Fzh-hans%2Fbitcoin%2Ftx-list",
    "oklink.unaccept_cookie": "1",
    "_monitor_extras": "{\"deviceId\":\"B4jum4L-mBmXnsuPAWVgAi\",\"eventId\":9,\"sequenceNumber\":9}",
    "okg.currentMedia": "sm",
    "ok-ses-id": "+ufqt72XWE1Dv6vTXsHaLdR5mxkpDShzZ9J/KxjFwkP5nP9/r5Ustf92lR4qKA7hGX/pMA7Q/wPwKzLR6OBTjIGYGiuWG+TNfj3QOWUuf9rtr6YtHDvrI8xMW28fm10Y"
}
response = requests.get(url,headers=headers, cookies=cookies)
print(response.json())