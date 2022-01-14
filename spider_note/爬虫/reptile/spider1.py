
import urllib.request
from lxml import html
import requests
import http.cookiejar
import urllib.parse
from urllib.request import urlopen
from bs4 import BeautifulSoup

def main():
    url = "https://wenshu.court.gov.cn/website/wenshu/181107ANFZ0BXSK4/index.html?docId=28b667cebe54480a9049acc201308ee4"
    header = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36 Edg/96.0.1054.29"
    }
    req = urllib.request.Request(url,headers=header)
    response = urllib.request.urlopen(req)
    html = response.read().decode("utf-8")
    print(html)
    file = open("data1.txt", "w")
    file.write(html)

def login_web(login_url):

    agent = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36 Edg/96.0.1054.29"

    cookie = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))

    header = {"User-Agent":agent}
    postdata = urllib.parse.urlencode({'u':'13184643209','p':'2020NJdx'})
    postdata=postdata.encode('UTF-8')

    request = urllib.request.Request(login_url,postdata,header)
    result = opener.open(request)
    html = result.read()
    bs = BeautifulSoup(html,"html.parser")

    print(bs.p)




if __name__ == "__main__":
    # login_web("https://wenshu.court.gov.cn/website/wenshu/181107ANFZ0BXSK4/index.html?docId=28b667cebe54480a9049acc201308ee4")
    main()