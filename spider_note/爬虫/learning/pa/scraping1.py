import urllib.request
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

def main():


    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }
    url = 'http://book.zongheng.com/'
    req = urllib.request.Request(url,headers=header)
    html = urlopen(req)
    #bs = BeautifulSoup(html,'html.parser')
    print(html.read().decode(''))

def test():
    url = 'http://book.zongheng.com'
    response = urlopen(url)
    content = response.read().decode('gbk','ignore').encode('utf-8').decode('utf-8')
    print(content)
if __name__ == '__main__':
    # main()
    test()