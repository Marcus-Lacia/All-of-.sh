

import requests
# import glob
# path1 = "/6/*.txt"
# for filename in glob.glob(path):
textdata = open('333.txt').read()


f=open(r'cook.txt','r')
cookies={}
for line in f.read().split(';'):  
    
    name,value=line.strip().split('=',1)
    cookies[name]=value  
S = requests.Session()

URL = "https://wiki.biligame.com/你的wiki/api.php"  #此处需要修改

# Step 1
PARAMS_0 = {
    "action": "query",
    "meta": "tokens",
    "type": "login",
    "format": "json"
}

R = S.get(url=URL,cookies=cookies, params=PARAMS_0)
DATA = R.json()

LOGIN_TOKEN = DATA['query']['tokens']['logintoken']

# Step 2
# supported. Obtain credentials via Special:BotPasswords
# (https://www.mediawiki.org/wiki/Special:BotPasswords) for lgname & lgpassword
PARAMS_1 = {
    "action": "login",
    "lgname": "帐号ID",#此处需要修改（可改可不改）
    "lgpassword": "密码",#此处需要修改（可改可不改）
    "lgtoken": LOGIN_TOKEN,
    "format": "json"
}

R = S.post(URL,cookies=cookies, data=PARAMS_1)

# Step 3: 
PARAMS_2 = {
    "action": "query",
    "meta": "tokens",
    "format": "json"
}

R = S.get(url=URL,cookies=cookies, params=PARAMS_2)
DATA = R.json()

CSRF_TOKEN = DATA['query']['tokens']['csrftoken']

# Step 4:
#关于此处的编辑语法可以参照你wiki的api.php
PARAMS_3 = {
    "action": "edit", #此处需要修改
    "title": "wiki的标题",#此处需要修改
    "appendtext": "wiki要填的内容",#此处需要修改
    "token": CSRF_TOKEN,
    "format": "json"
}

R = S.post(URL,cookies=cookies, data=PARAMS_3)
DATA = R.json()

print(DATA)
