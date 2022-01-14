import urllib.request

# 获取一个get请求
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8')) # 对获取到的网页源码进行utf-8解码


# 获取一个post请求
# 模拟用户登录，发送表单
# import urllib.parse
# data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding='utf-8')
# response = urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(response.read().decode('utf-8'))


# 超时处理 try-catch
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get",timeout=0.01)
#     print(response.read().decode('utf-8'))
# except urllib.error.URLError as e:
#     print("time out!")


# response = urllib.request.urlopen("http://www.baidu.com")
# # print(response.status)
# print(response.getheaders())


# 模拟浏览器的访问

# url = "https://www.douban.com"
# url = "http://httpbin.org/post"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36 Edg/96.0.1054.29"
# }
# data = bytes(urllib.parse.urlencode({'name':'eric'}),encoding="utf-8")
# # 请求头的封装
# req = urllib.request.Request(url=url,data=data,headers=headers,method="POST")
#
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))

url = "https://www.douban.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36 Edg/96.0.1054.29"
}
req = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))



