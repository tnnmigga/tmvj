import requests


class HdojAccount():
    username = ''
    password = ''
    account = None
    local_session = None
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Host": "httpbin.org",
        "Referer": "https://blog.csdn.net/XnCSD/article/details/88615791",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edg/81.0.416.72",
        "X-Amzn-Trace-Id": "Root=1-5ebac5d5-7504aa38c63a9fb567cabbe3"
    }

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.local_session = requests.session()

    def login(self):
        url = 'http://acm.hdu.edu.cn/userloginex.php?action=login'

        profile = {
            'username': self.username,
            'userpass': self.password,
            'login': 'Sign+In'
        }

        self.account = self.local_session.post(
            url=url, data=profile, headers=self.headers)
        print(self.account.status_code)
        #test = requests.get(url='http://acm.hdu.edu.cn/showproblem.php?pid=1037', cookies=self.request.cookies)
        # print(test.text)

    def submit(self, problemid, usercode, language):
        url = 'http://acm.hdu.edu.cn/submit.php/submit.php?action=submit?'

        data = {
            'problemid': problemid,
            'usercode': usercode
        }

        if language == 'cpp':
            data['language'] = 1
        elif language == 'java':
            data['language'] = 2
        else:
            data['language'] = 6

        submit = requests.post(
            url=url, data=data, headers=self.headers, cookies=self.account.cookies)
        print(submit.text)


hdu = HdojAccount('tangmingvj', 'qq123456')
hdu.login()
hdu.submit(1000, '0' * 500, 'cpp')
