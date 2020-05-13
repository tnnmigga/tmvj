import requests


class HdojAccount():
    username = ''
    password = ''
    account = None
    local_session = None

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.local_session = requests.session()

    def login(self):
        url = 'http://acm.hdu.edu.cn/userloginex.php?action=login'

        data = {
            'username': self.username,
            'userpass': self.password,
            'login': 'Sign+In'
        }

        headers = {
            "Host": "acm.hdu.edu.cn",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Accept-Encoding": "gzip, deflate",
            # "Content-Type": "application/x-www-form-urlencoded",
            # "Content-Length": "33",
            # "Origin": "http://acm.hdu.edu.cn",
            "Connection": "keep-alive",
            "Referer": "http://acm.hdu.edu.cn/",
            "Cookie": "PHPSESSID=bd3an4n6gf07qhqn01adm5apn0",
            "Upgrade-Insecure-Requests": "1"
        }

        self.account = self.local_session.post(
            url=url, data=data, headers=headers, allow_redirects=False)
        print(self.account.status_code)
        #test = requests.get(url='http://acm.hdu.edu.cn/showproblem.php?pid=1037', cookies=self.account.cookies)
        #print(test.text)

    def submit(self, problemid, usercode, language):
        url = 'http://acm.hdu.edu.cn/submit.php/submit.php?action=submit?'

        data = {
            'problemid': problemid,
            'usercode': usercode
        }

        headers = {
            "Host": "acm.hdu.edu.cn",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Accept-Encoding": "gzip, deflate",
            # "Content-Type": "application/x-www-form-urlencoded",
            # "Content-Length": "33",
            # "Origin": "http://acm.hdu.edu.cn",
            "Connection": "keep-alive",
            "Referer": "http://acm.hdu.edu.cn/showproblem.php?pid=" + str(problemid),
            "Cookie": "PHPSESSID=bd3an4n6gf07qhqn01adm5apn0",
            "Upgrade-Insecure-Requests": "1"
        }

        if language == 'cpp':
            data['language'] = 1
        elif language == 'java':
            data['language'] = 2
        else:
            data['language'] = 6

        submit = requests.post(
            url=url, data=data, headers=headers, cookies=self.account.cookies)
        #print(submit.text)
        print(submit.url)


hdu = HdojAccount('tangmingvj', 'qq123456')
hdu.login()
hdu.submit(1002, '0' * 500, 'cpp')
