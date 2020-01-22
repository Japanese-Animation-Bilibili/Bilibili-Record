import requests

history_url = 'http://api.bilibili.cn/history'
user_agent = 'history/1.0.0(panyuyuyu@outlook.com)'
headers = { 'User-Agent': user_agent }

def get_history():
    response = requests.get(history_url, headers=headers)
    print(response.text)


get_history()