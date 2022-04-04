html_doc = '''
<html>
    <head>
        <title>Test Page</title>
    </head>
    <body>
        <h1>Hello World</h1>
    </body>
</html>
'''

from urllib import request
from bs4 import BeautifulSoup

content = request.urlopen('http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1174051500')
soup = BeautifulSoup(content, 'html.parser')

for data in soup.select('data'):
    print('day:', data.select_one('day'))
    print('weather:', data.select_one('wfkor'))
    print('-' * 20)