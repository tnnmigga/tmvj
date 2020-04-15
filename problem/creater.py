import requests
import re

title_re=re.compile(r"<h1 style='color:#1A5CC8'>(.*?)</h1>")

def get_problem_detail(problem_id):
    url = 'http://acm.hdu.edu.cn/showproblem.php'
    params = {'pid': str(problem_id)}
    http_response = requests.get(url=url, params=params)
    html = http_response.text
    title = re.search(r"<h1 style='color:#1A5CC8'>(.*?)</h1>", html).group(1)
    input_description = re.search(r'<div class="panel_content">(.*?)</div>', html).group(1)
    
    #print(html)
    print(input)

