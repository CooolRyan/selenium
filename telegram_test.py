import http.client
import json

TELEGRAM_API_HOST = 'api.telegram.org'
TOKEN = '5332269332:AAHbTs0Za5GFqPKQsNjP1eo4ANmaW93pqr0'

connection = http.client.HTTPSConnection(TELEGRAM_API_HOST)

# 토큰과 메서명 지정
url = f"/bot{TOKEN}/sendMessage"

# HTTP 헤더
headers = {'content-type': "application/json"}

# 파라미터
param = {
    'chat_id': 1469553600,
    'text': 'python 에서 보냄'
}

# Http 요청
connection.request("POST", url, json.dumps(param), headers)

# 응답
res = connection.getresponse()

# Response body 출력
print(json.dumps(json.loads(res.read().decode()), indent=4))
print('응답코드 : ', res.status)
print('메시지 : ', res.msg)

# 연결 끊기
connection.close()