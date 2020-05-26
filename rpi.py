import requests
from bs4 import BeautifulSoup

url = "https://roundcube.rpi.edu/roundcube/"
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
rpimail = requests.Session()
res = rpimail.get(url,headers=headers)
soup = BeautifulSoup(res.text,'html.parser')
inputdata =  soup.findAll('input')
gettoken = str(inputdata[0].get('value'))
print(gettoken)
print(len(gettoken))
payload ={
    '_token' : gettoken,
    '_user' : '----',
    '_pass' : '------',
    '_action' : 'login',
    '_task' : 'login',
    '_timezone' : 'Asia/Shanghai'
}
mail= rpimail.post(url, headers=headers, data=payload)
print(mail.text)
