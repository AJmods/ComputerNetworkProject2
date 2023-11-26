import html
from http import client
import requests
host = '13.125.255.214'
port = 51957
user_agent = '9169920236/DANDA ANDREW/WEBCLIENT/COMPUTERNETWORK'
# r=requests.get("http://13.125.255.214:62592/test/index.html", headers={"Content-Type":"text",'User-agent': '9169920236/DANDAANDREW/WEBCLIENT/COMPUTERNETWORK'})
# print(r)

conn = client.HTTPConnection(host + ":" + str(port))
# print(conn)
conn.request("GET", "/test/index.html", headers={"HOST":host, "user-agent":user_agent})
response = conn.getresponse()
print(response.status, response.reason)
#print(response.headers)
print(response.msg)
htmlRes = response.read().decode()
print(htmlRes)
images = 16 - htmlRes.count('src="null')
print("images", images)

print()
print("posting result")
url = "http://" + host + ":" + str(port) + "/test/result.html"
params = {"stuAnswer": images, "sno1": 9169920236}
x = requests.post(url, data=params)
#conn.request("POST", "/test/result.html", json=params) #headers={"user-agent":user_agent})
#res2 = conn.getresponse()
print(x.text)

print("\nMission 3")

url = "http://" + host + ":" + str(port) + "/test/postHandleTest.html"
params = {"stuAnswer": images, "sno1": 9169920236}
x = requests.post(url, data=params)
#conn.request("POST", "/test/result.html", json=params) #headers={"user-agent":user_agent})
#res2 = conn.getresponse()
print(x.text)

# conn.request("GET", "test/postHandleTest.html", headers={"HOST":host, "user-agent":user_agent})
# res3 = conn.getresponse()
# print(res3.status, res3.reason)
# print(res3.headers)
# #print(response.getheader())
# print()
