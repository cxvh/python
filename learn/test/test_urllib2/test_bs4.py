'''
Created on 2020年1月20日

@author: Baran
'''
from bs4 import BeautifulSoup
import re
html_doc = """
<html>
    <head>
        <title>这是一个标题</title>
    </head>
    <body>
        <h5>内容标题</h5>
        <p class="des">内容描述</p>
        <div class="link">
            <a href="http://www.baidu.com">链接1</a>
            <a href="http://www.qq.com">链接2</a>
            <a href="http://www.iqiyi.com">链接3</a>
        </div>
        <p class="foot">底部1</p>
        <p class="foot" id="a1">底部2</p>
    </body>
</html>
"""

soup = BeautifulSoup(html_doc,'html.parser',from_encoding='utf-8')

print('获取所有链接')
links=soup.find_all('a')

for link in links:
    print(link.name,link['href'],link.get_text())
    
print('获取链接2的链接')
link_node=soup.find('a',href="http://www.qq.com")
print(link_node.name,link_node['href'],link_node.get_text())

print('正则匹配')
link_node=soup.find('a',href=re.compile(r"qiyi"))
print(link_node.name,link_node['href'],link_node.get_text())

print('获取p文字')
p_node=soup.find('p',class_="des")
print(p_node.name,p_node.get_text())

print('获取p id文字')
pid_node=soup.find('p',id="a1")
print(pid_node.name,pid_node.get_text())
