import requests


class HdojAccount():
    username = ''
    password = ''
    request = None

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        url = 'http://acm.hdu.edu.cn/userloginex.php?action=login'
        headers = {'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
                   'Accept - Encoding': 'gzip, deflate',
                   'Accept-Language': 'zh-Hans-CN, zh-Hans; q=0.5',
                   'Connection': 'Keep-Alive',
                   'Host': 'zhannei.baidu.com',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}

        profile = {
            'username': self.username,
            'userpass': self.password
        }

        self.request = requests.post(url=url, data=profile, headers = headers)

        print(self.request.text)

hdu = HdojAccount('tnnmigga', 'qwertyuiop4096')
hdu.login()
