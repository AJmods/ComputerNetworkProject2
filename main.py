import http
from http import client
import requests
host = '13.125.255.214'
port = 62632
user_agent = '9169920236/DANDAANDREW/WEBCLIENT/COMPUTERNETWORK'
# r=requests.get("http://13.125.255.214:62592/test/index.html", headers={"Content-Type":"text",'User-agent': '9169920236/DANDAANDREW/WEBCLIENT/COMPUTERNETWORK'})
# print(r)

conn = client.HTTPConnection(host + ":" + str(port))
print(conn)
conn.request("GET", "/test/index.html", headers={"HOST":host, "user_agent":user_agent})
response = conn.getresponse()
print(response.status, response.reason)
print(response.headers)
print(response.getheader())
print()
